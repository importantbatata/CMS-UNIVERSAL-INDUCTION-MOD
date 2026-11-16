<div align="center">

# CMS Universal Induction Mod

### Build your boost. Choose your setup.

**Turbo · Roots Supercharger · ProCharger P-1X**  
Custom forced induction for **Car Mechanic Simulator 2018**.

![Game: CMS 2018](https://img.shields.io/badge/CAR_MECHANIC_SIMULATOR-2018-252b36?style=for-the-badge)
![Version: 0.8.87](https://img.shields.io/badge/VERSION-0.8.87-00a8a8?style=for-the-badge)
![Status: pre-release](https://img.shields.io/badge/STATUS-PRE--RELEASE-f5a623?style=for-the-badge)

**[↓ Download v0.8.87](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/releases/tag/v0.8.87)** · **[All releases](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/releases)** · **[Report a bug](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/issues)**

---

</div>

## More ways to build your engine

Bring custom forced-induction setups into your CMS 2018 garage. Choose an induction type on the engine stand, experiment with boost and turbo sizing, and fit a custom setup to your build.

This BepInEx/Harmony mod combines induction selection, shop integration, visual components, engine-transfer handling, and estimated boost/dyno behavior. It is actively being developed toward **v1.0**; models, fitment, and gameplay behavior are still being refined.

| TURBO | ROOTS SUPERCHARGER | PROCHARGER P-1X |
| :--- | :--- | :--- |
| Selectable **35–88 mm** inducer tiers | A Roots-style induction option | Custom centrifugal-supercharger model |
| Estimated size-dependent spool, flow and boost | Uses copied native CMS visual assets | Pulley, belt, bracket, intake hose and charge-pipe visuals |
| Bounded compressor and charge-air calculations | Side-mounted visual setup under development | Standard and **32 PSI** shop variants |

## Inside the mod

- **Engine-stand selection** — choose an induction setup through the “Add forced induction” radial-menu action.
- **Garage visuals** — Turbo, Roots and P-1X setups, with ongoing placement and transfer fixes.
- **Shop integration** — standard P-1X in Main Shop at **$12,500** and high-boost P-1X in Tuning Shop at **$24,900**.
- **Boost and sizing controls** — turbo tiers from **35, 45, 55, 62, 67, 76 to 88 mm**, with saved settings.
- **Estimated performance** — modeled spool, airflow, compressor efficiency and charge-air effects for the existing dyno path.
- **Mods menu** — an in-game page for loaded BepInEx plugins.

> **Development build:** Features above are implemented prototype systems. Compatibility and behavior vary by engine and patch; offline checks do not establish that every feature works in-game.

## Get started

1. **Download the mod ZIP** from [v0.8.87](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/releases/tag/v0.8.87). Choose **CMS18TurboPrototype-0.8.87.zip** under Assets.
2. **Close CMS 2018** and back up your existing plugin and save profile before trying a pre-release.
3. With a working **BepInEx** installation for CMS 2018, extract the package and place `CMS18TurboPrototype.dll` in `BepInEx/plugins/`. Follow the package report for any included asset/setup requirements. Replace the previous plugin rather than loading duplicate versions.
4. Launch the game, confirm the plugin version in `BepInEx/LogOutput.log`, and try the engine-stand induction chooser.

The release ZIP includes the versioned package. Its README and report contain patch-specific details; GitHub’s automatic **Source code** archives are repository snapshots, not the packaged mod download.

## Latest pit stop · v0.8.87

**ProCharger shop-listing repair.** Custom catalog entries now use the base-game product marker so both P-1X variants can pass the shop’s DLC visibility check.

Build and offline validation passed. **Live shop visibility, buying and removal still need a retest.** Visible bolt heads are decorative; the current mount uses the part’s **one-action take-off prompt**.

[Read the release notes →](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/releases/tag/v0.8.87)

## Compatibility & current limits

| Area | Current status |
| :--- | :--- |
| Game | **Car Mechanic Simulator 2018** |
| Release channel | **Pre-release / in development** |
| Engine coverage | Universal fitment is the goal; broad engine compatibility is still being verified |
| DLC cars | **Not supported at present**; the developer does not own all DLCs for testing |
| 3D models | Work in progress; appearance and fitment are not final |
| Performance numbers | Game-model estimates, not measured real-world compressor maps |
| Latest gameplay validation | Shop, removal, dyno and save/load behavior still require live checks |

## Road to v1.0

The next steps are to refine what is already in the garage and build out the larger induction system:

- Improve fitment, engine transfer, selection and removal across more engines.
- Verify shop visibility, dyno behavior, save/load and isolation between cars.
- Build a physical turbo component/dependency chain and supporting hardware.
- Expand configurations, engine coverage, durability and persistence.

Twin, sequential, compound and twincharged setups, complete supporting-parts systems, and broad verified engine support are **not complete**. All current releases remain pre-releases.

## Help shape the next patch

Found something wrong? [Open an issue](https://github.com/importantbatata/CMS-UNIVERSAL-INDUCTION-MOD/issues) with the **mod version**, **engine/car**, what you expected, what happened, and steps to reproduce it. Screenshots and the relevant section of `BepInEx/LogOutput.log` help with visual and runtime bugs.

---

<div align="center">

**A garage project, still gaining boost.**  
Built for CMS 2018 · Actively developed toward v1.0

</div>
