# ProCharger v0.9.20

This release fits a dedicated 19 mm ProCharger drive belt to the 22 engines tagged as base game in the CMS 2018 Engine Shop catalog. It aligns the drive with each crankshaft, keeps the ProCharger belt outboard of the factory belts, and uses a separate running surface at a factory guide or water-pump pulley. The stock supercharged V8s use a lateral offset for blower clearance.

Engine fitment.csv records the route and factory-belt clearance for each engine. Those checks used stock engine-prefab mesh bounds and the compiled belt planner. They cover fully assembled stock engines. Live engine-stand interaction and clearance inside individual car bodies have not been verified across the full list.

The ZIP includes the plugin DLL, editable source, and model. Only CMS18TurboPrototype.dll belongs in BepInEx/plugins. Close CMS before installing a different version and keep the previous DLL outside the plugins folder.
