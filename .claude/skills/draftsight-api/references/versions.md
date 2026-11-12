# Versions
## Release names and `since`
- The bundled data is the API help shipped with DraftSight 2026 SP4. Its Release Notes topic still describes the 2024 API, and the newest `since` in the data is 2024 SP4 (for example `IApplication.GetFileDialogManager`, `_IApplicationEvents.OnFileProcessedNotify`, the `IMLeader` members). The help documents no members added in 2025 or 2026, so the documented API is the same on 2024 SP4, 2025 and 2026.
- Releases before 2016 SP1 used `V1R` names: `V1R1.0` to `V1R1.4`, `V1R2.0` and `V1R2.1`, `V1R3.0` and `V1R3.1`, `V1R4.0`, `V1R5.0` and `V1R5.1`, `V1R6.0`. The data keeps these names as `since`, and `check --target` orders them before all dated releases, so `--target V1R5.0` and `--target 2017` both work. About three quarters of the API dates from `V1R` releases.
- Dated releases follow the pattern `2017`, `2018 SP2`, `2020 SP3`, `2024 SP4`; a bare year means SP0.
- `IApplication.GetVersion` returns the running release string; report it when debugging version problems.
## Targeting an older install
1. Ask for the oldest release the code must run on, and run `swapi.py check FILE --target RELEASE` on every file.
2. For each `since` finding, take the obsolete predecessor whose `since` fits (see [version availability](correctness-rules.md#version-availability)) and say in the answer that the newer member is preferred on newer installs.
3. Test on the oldest target release. The newest interop and type library accept members the older install lacks, and those calls fail only at run time.
4. After any DraftSight upgrade, re-add VBA type library references and .NET interop references, as the Getting Started topic requires.
## What a release added
- `swapi.py topic "Release Notes"` prints the help's release notes, grouped by service pack, with every new interface and member.
- `swapi.py members INTERFACE` shows `since` per member; `find` rows show it per result.
- `swapi.py changes --since "2024 SP2"` lists every member whose `since` is that release or later, grouped by interface. Without `--since`, `changes` compares with previously bundled data, which this first DraftSight data set does not have.
## Editions
Some members need a specific DraftSight edition, and their Remarks say so: macro recording through `IApplication.GetMacroManager` is DraftSight Premium only, and the 3D modeling members on `ISketchManager` need DraftSight Premium or Enterprise Plus. The `premiumOnly` attribute of an add-in's `addinConfigs` XML decides which editions load it ([dotnet.md](dotnet.md#registration)). Mac and Linux support only the C++ and JavaScript interfaces, according to the help's Welcome topic.
