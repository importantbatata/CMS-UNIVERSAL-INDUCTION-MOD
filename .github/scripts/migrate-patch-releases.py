import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

repository = os.environ['GITHUB_REPOSITORY']
token = os.environ['GITHUB_TOKEN']
target = '7beab502c8d1db8a177685b8f06f1f2336f8e83f'
api = 'https://api.github.com/repos/' + repository


def request(url, data=None, content_type='application/json'):
    headers = {'Authorization': 'Bearer ' + token,
               'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28',
               'User-Agent': 'CMS18-release-migration'}
    if data is not None:
        headers['Content-Type'] = content_type
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=120) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


manifest = json.loads(Path('PATCH-MANIFEST.json').read_text())
packages = sorted((entry for entry in manifest if entry['location'] == 'repository'),
                  key=lambda entry: tuple(map(int, entry['version'].split('.'))))
assert len(packages) == 39
verified = []
for package in packages:
    version = package['version']
    tag = 'v' + version
    archive = Path(package['download'])
    data = archive.read_bytes()
    digest = 'sha256:' + hashlib.sha256(data).hexdigest()
    assert digest == 'sha256:' + package['sha256'], archive
    procharger = version.startswith('0.9.')
    current = version == '0.9.20'
    title = ('ProCharger P-1X' if procharger else 'Legacy induction') + ' ' + version
    if current:
        title += ' — Base-game drive fitment'
    else:
        title += ' — ' + package['description'].split(';')[0].rstrip('.')
    body = '## ' + ('ProCharger P-1X' if procharger else 'Historical development archive') + '\n\n'
    body += package['description'] + '\n\n'
    if current:
        body += ('### What changed\n\n'
                 '- Dedicated 19 mm ProCharger drive belt aligned to the crankshaft.\n'
                 '- Separate belt tracks and engine-specific routing for 22 base-game catalog engines.\n'
                 '- Lateral adjustments for factory-supercharged V8 layouts.\n'
                 '- Engine fitment CSV included in the original package.\n\n'
                 'The package author reports offline checks using fully assembled stock engine-prefab mesh bounds '
                 'and the compiled belt planner. Live engine-stand interaction and clearance inside individual car bodies '
                 'have not been verified across all 22 engines.\n\n')
    elif not procharger:
        body += ('**Legacy archive:** this superseded version may contain retired turbocharger, Roots-supercharger, '
                 'or ECU Lab systems and known development defects. The active project is ProCharger-only. '
                 'Use [0.9.20](https://github.com/' + repository + '/releases/tag/v0.9.20) for the current package.\n\n')
    else:
        body += ('This is a historical ProCharger-only snapshot. Use [0.9.20](https://github.com/' + repository +
                 '/releases/tag/v0.9.20) for the current package.\n\n')
    body += ('### Download and install\n\n'
             'Download **' + archive.name + '** under Assets. Each patch ZIP is a complete version snapshot; '
             'do not install versions cumulatively. Close CMS 2018, keep the previous DLL outside the plugins folder, '
             'and install the package’s CMS18TurboPrototype.dll into BepInEx/plugins with BepInEx and Harmony available. '
             'Follow any included package README/report for version-specific requirements.\n\n'
             'The named ZIP preserves the supplied package, including source where provided. GitHub’s automatic '
             'Source code archives are repository documentation snapshots, not the version-specific mod package.\n\n'
             '### Integrity and validation\n\n'
             'SHA-256: `' + package['sha256'] + '`\n\n'
             'Original package bytes preserved. Release descriptions were derived from supplied reports and source '
             'comparisons; no build or in-game testing was performed during publication. All versions remain development builds.\n\n'
             '[Patch catalog](https://github.com/' + repository + '/blob/main/PATCHES.md) · '
             '[Report an issue](https://github.com/' + repository + '/issues)\n')
    try:
        release = request(api + '/releases/tags/' + tag)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
        release = request(api + '/releases', json.dumps({
            'tag_name': tag, 'target_commitish': target, 'name': title,
            'body': body, 'draft': False, 'prerelease': True,
            'make_latest': 'false'}).encode())
    assets = request(api + '/releases/' + str(release['id']) + '/assets?per_page=100')
    asset = next((item for item in assets if item['name'] == archive.name), None)
    if asset is None:
        upload = release['upload_url'].split('{')[0] + '?name=' + urllib.parse.quote(archive.name)
        asset = request(upload, data, 'application/zip')
    assert asset['size'] == len(data), archive.name
    assert asset.get('digest') == digest, archive.name
    assert not release['draft']
    verified.append({'version': version, 'release': release['html_url'],
                     'asset': asset['browser_download_url'], 'sha256': package['sha256']})
    print('Verified ' + tag + ': ' + archive.name, flush=True)

assert len(verified) == 39
Path('release-migration-results.json').write_text(json.dumps(verified, indent=2))
with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
    summary.write('## Release migration complete\n\n39 published packages verified by SHA-256.\n\n')
    for result in reversed(verified):
        summary.write('- [' + result['version'] + '](' + result['release'] + ')\n')
