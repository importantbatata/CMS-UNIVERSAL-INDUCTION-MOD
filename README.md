<div align="center">

# CMS 2018 ProCharger P-1X

### A focused build. A dedicated drive. Centrifugal boost.

**ProCharger-only development mod for Car Mechanic Simulator 2018**

**[Download v0.9.20](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/releases/tag/v0.9.20)** · **[Patch catalog](PATCHES.md)** · **[Report an issue](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/issues)**

</div>

CMS 2018 ProCharger P-1X adds standard and high-boost centrifugal-supercharger kits to the garage, with shop integration, native installation and removal flows, a custom P-1X visual, a dedicated belt drive, and modeled boost and dyno behavior.

**The active project is now ProCharger-only.** The mod's turbocharger, Roots-supercharger, and ECU Lab features were retired in the 0.9 series. Older packages remain available as historical development snapshots; their features and test records do not describe the current build. The repository URL and `CMS18TurboPrototype.dll` filename are retained for continuity.

## Latest: 0.9.20

The latest supplied package focuses on the P-1X drive across **22 engines identified as base-game entries in the CMS 2018 Engine Shop catalog**:

- A dedicated **19 mm drive belt**, aligned to each crankshaft axis.
- Routing outboard of the factory belts, with a separate running surface at a factory guide or water-pump pulley.
- Engine-specific placement adjustments, including lateral clearance for stock supercharged V8 layouts.
- An included [engine fitment table](docs/Engine%20fitment.csv) recording the route and measured planning clearances.

The package author reports checks using stock engine-prefab mesh bounds and the compiled belt planner on fully assembled stock engines. **These are offline fitment checks: live engine-stand interaction and clearance inside individual car bodies have not been verified across all 22 engines.** This import did not run the game or rebuild the plugin.

## What the current mod includes

| System | Current scope |
| --- | --- |
| Kits | Standard P-1X and P-1X High-Boost, registered with CMS shops. |
| Installation | Engine-stand actions and the native inventory selector; a purchased, owned kit is required. |
| Removal | Four P-1X flange bolts and a removal animation in the current source. |
| Boost setup | Native radial controls, with targets bounded by the installed kit's rating. |
| Presentation | Custom P-1X model, pulley/belt geometry, hover highlighting, and boost/vacuum display. |
| Performance | P-1X-specific centrifugal calculations and scoped dyno integration; values are game-model estimates. |
| Persistence | Existing plugin identity and part IDs retained, with engine-transfer and installed-kit tracking. |

The current source also models a 15% larger oil-fill capacity for the fitted P-1X circuit. This is game behavior implemented by the mod, not a real-world installation specification.

## Kits and shops

| Kit | Shop | Base price | Modeled boost-target ceiling |
| --- | --- | ---: | ---: |
| ProCharger P-1X | Main Shop | $12,500 | 20 PSI |
| ProCharger P-1X High-Boost | Tuning Shop | $24,900 | 32 PSI |

Targets are settings, not guaranteed delivered pressure or power. Results depend on the modeled operating conditions and game integration. The mod does not claim validated real-world compressor-map accuracy or universal vehicle compatibility.

## Installation and updating

1. Close Car Mechanic Simulator 2018. Use a working BepInEx installation with Harmony (`0Harmony.dll`).
2. Open the [**v0.9.20 release**](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/releases/tag/v0.9.20) and download **CMS18-ProCharger-P1X-0.9.20.zip** under Assets.
3. Extract the ZIP. Copy **only `CMS18TurboPrototype.dll`** into the game's `BepInEx/plugins/` folder.
4. Replace the older copy. Keep any rollback DLL outside `BepInEx/plugins/` so two versions cannot load together.
5. Launch CMS 2018 and check `BepInEx/LogOutput.log` for **CMS 2018 ProCharger P-1X 0.9.20** and any patch errors.
6. Buy a P-1X kit in its shop, place an engine on the stand, and use the ProCharger radial actions and native inventory picker to install it.

```text
Car Mechanic Simulator 2018/
└── BepInEx/
    └── plugins/
        └── CMS18TurboPrototype.dll
```

The model is embedded by the build; source files and loose models do not belong in the plugins folder. Choose the named mod ZIP under release **Assets** for the plugin and editable package source. GitHub’s automatic **Source code** archives are repository snapshots, not the version-specific mod package.

Legacy non-ProCharger mode values are migrated to Off in the current source. Old turbo/Roots identifiers remain only for recognizing legacy saved custom parts, not as supported shop or performance options. Preserve a backup of an older save before moving a historical development build to the current version.

## Source and building

The latest mod ZIP includes `src`, `model`, `build.ps1`, the supplied DLL, and its original README and fitment CSV. The supplied Windows build script compiles `CMS18TurboPrototype.cs`, `ChargeAirModel.cs`, and `ProchargerMath.cs`, and embeds `model/CMS18_ProCharger_P1X.obj`.

The script uses the .NET Framework 64-bit compiler and references your installed CMS, Unity, BepInEx, and Harmony assemblies. Its game path is currently hard-coded to the default Steam location; edit `$game` if your installation differs. From the extracted package, run:

```powershell
.\build.ps1
```

The output goes to `build/CMS18TurboPrototype.dll`. Optional `-Install` and `-ReplaceInstalled` switches exist in the supplied script; installation checks that CMS is closed and backs up an existing DLL before replacing it when explicitly requested. Game dependencies are not bundled in this repository.

## Patch history without duplicate downloads

[PATCHES.md](PATCHES.md) indexes every numbered patch supplied in this import. Existing releases remain the download location for packages already published. Only the **39 missing packages** were selected for upload: published as individual versioned GitHub Releases, including the current 0.9.20 package. Download ZIPs are kept in Releases; the repository contains the README, catalog, manifest, and fitment documentation.

All releases are marked as development pre-releases. Older versions can contain retired systems and known defects. Install one complete version at a time; patch numbers here identify full packaged snapshots rather than incremental updates to apply in sequence. Read the descriptions and any included reports before using an archived build.

## Compatibility and verification

- **Game:** Car Mechanic Simulator 2018; supplied build tooling targets Windows.
- **Current development version:** 0.9.20. Broad live vehicle-body fitment and engine interaction coverage remain unverified.
- **Engine coverage:** 22 cataloged base-game engine layouts have offline drive-planner records; DLC compatibility is not established by that table.
- **Models and performance:** still under development. Offline geometry/model checks do not prove live installation, transfer, removal, save/load, or dyno behavior.
- **Import checks:** all 71 supplied patch ZIPs passed ZIP integrity checks. Missing-package archives are preserved byte-for-byte, with SHA-256 values recorded in [PATCH-MANIFEST.json](PATCH-MANIFEST.json).

If you encounter a problem, include the version, engine/car, steps to reproduce, screenshots where relevant, and the matching section of `BepInEx/LogOutput.log` in an [issue](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/issues). Useful regression checks include buying both kits, native install/remove, all four bolts, engine transfer, per-car isolation, boost setup, and factory-versus-measured dyno output.

---

Unofficial game mod. Not affiliated with or endorsed by the game's developers or publishers, or by ProCharger. Product names identify the modeled component.
