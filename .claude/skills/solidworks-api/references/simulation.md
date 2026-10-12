# Simulation API
Automating SOLIDWORKS Simulation studies (module `cworksapi`, interop `SolidWorks.Interop.cosworks`): getting the add-in, creating studies, materials, fixtures, loads, mesh, running and reading results.
## Contents
- [Prerequisites](#prerequisites)
- [Getting the Simulation object](#getting-the-simulation-object)
- [Studies](#studies)
- [Materials](#materials)
- [Fixtures and loads](#fixtures-and-loads)
- [Mesh and run](#mesh-and-run)
- [Results](#results)
- [Units and errors](#units-and-errors)
## Prerequisites
- The SOLIDWORKS Simulation add-in must be loaded (Tools > Add-Ins, or `ISldWorks.LoadAddIn`) and licensed; nonlinear and dynamic study types need the higher Simulation tiers.
- A SOLIDWORKS document must be open and active before a study can be created.
- References: `SolidWorks.Interop.cosworks` next to the core interops ([dotnet-addins.md](dotnet-addins.md#project-and-interop-references)); VBA references the SOLIDWORKS Simulation type library. Look members up with `swapi.py find QUERY --module cworksapi`; Simulation members report availability as `SOLIDWORKS Simulation API <year>`.
## Getting the Simulation object
- `ISldWorks.GetAddInObject(progId)` returns the Simulation add-in object; its `CosmosWorks` property returns `ICosmosWorks`. The C# examples cast the result to `CwAddincallback` (and some pass `CosmosWorks.CosmosWorks`).
- With several SOLIDWORKS releases installed, the version-independent ProgID `SldWorks.Simulation` resolves to the newest install and fails with type mismatches from an older session. Build the version-specific ProgID `SldWorks.Simulation.<n>` with n = major revision minus 15, the major revision being the first two digits of `ISldWorks.RevisionNumber` (27 is 2019, so `SldWorks.Simulation.12`; 2025 is 18, 2026 is 19).
- Test each object for null: an unloaded or unlicensed add-in returns Nothing ([null checks](correctness-rules.md#null-checks-and-return-values)).
- `ICosmosWorks.ActiveDoc` returns the `ICWModelDoc` of the active SOLIDWORKS document.
## Studies
- `ICWModelDoc.StudyManager` returns `ICWStudyManager`. Create with `ICWStudyManager.CreateNewStudy3(Name, swsAnalysisStudyType_e, SubOptions, out Errors)`; SubOptions matter only for dynamic (`swsDynamicAnalysisSubType_e`) and fatigue (`swsFatigueStudySubOption_e`) studies, and Errors is `swsStudyError_e`. `ICWStudyManager.CreateNewStudy2` is obsolete.
- Existing studies: `ICWStudyManager.StudyCount`, `ICWStudyManager.GetStudy(index)`, and `ICWStudyManager.ActiveStudy` to activate one.
- Study options: `ICWStudy.StaticStudyOptions` and the other per-type option objects.
## Materials
- Walk `ICWStudy.SolidManager` (`ICWSolidManager.ComponentCount`, `ICWSolidManager.GetComponentAt(i, out err)`), then `ICWSolidComponent.GetSolidBodyAt(j, out err)` to reach each `ICWSolidBody`.
- Assign library materials with `ICWSolidBody.SetLibraryMaterial2(libraryPath, materialName)` (2022 and later; `ICWSolidBody.SetLibraryMaterial` is obsolete); inspect them with `ICWSolidBody.GetSolidBodyMaterial` and `ICWMaterial.GetPropertyByName2`.
## Fixtures and loads
- `ICWStudy.LoadsAndRestraintsManager` returns `ICWLoadsAndRestraintsManager`.
- Fixtures: `ICWLoadsAndRestraintsManager.AddRestraint(swsRestraintType_e, Entities, RefGeom, out ErrorCode)`, for example `swsRestraintTypeFixed` on an array of faces; RefGeom is used only with `swsRestraintTypeReferenceGeometry`.
- Forces: `ICWLoadsAndRestraintsManager.AddForce3` takes the force type (`swsForceTypeNormal`, `swsForceTypeForceOrMoment`, `swsForceTypeTorque`), selection type, direction reference, table-driven and beam options, a component code (1 Fx, 2 Fy, 4 Fz, 8 Mx, 16 My, 32 Mz, summed; 0 for normal force), component values, the entity array and an error out parameter. Copy the argument order from `swapi.py sig` and an example (`swapi.py examples --symbol ICWLoadsAndRestraintsManager.AddForce3`) rather than from memory. `ICWLoadsAndRestraintsManager.AddForce2` is obsolete.
- Pressure: `ICWLoadsAndRestraintsManager.AddPressure(swsPressureType_e, Entities, RefGeom, out ErrorCode)`.
- Entity arrays hold SOLIDWORKS faces, edges or vertices: take them from the selection (`ISelectionMgr.GetSelectedObject6`), from named entities (`IPartDoc.GetEntityByName`), or from persistent IDs collected with `install_dir\api\pidcollector.exe`. In VBA pass them in a Variant; in .NET pass an `object[]` ([arrays and Variants](correctness-rules.md#arrays-and-variants)).
## Mesh and run
- `ICWStudy.Mesh` returns `ICWMesh`; set `ICWMesh.Quality` and `ICWMesh.MesherType`, get defaults with `ICWMesh.GetDefaultElementSizeAndTolerance(units, out size, out tolerance)`, then mesh with `ICWStudy.CreateMesh(units, size, tolerance)`, which returns an error code (0 is success).
- Run with `ICWStudy.RunAnalysis` (returns an error code); `ICWStudy.MeshAndRun` (2016 and later) does both.
## Results
- `ICWStudy.Results` returns `ICWResults` after a successful run.
- `ICWResults.GetMinMaxStress(swsStressComponent_e, element, step, plane, units, out ErrorCode)` returns `{minNode, minValue, maxNode, maxValue}`; use `swsStressComponentVON` for von Mises, step 1 for static studies, and Nothing for the plane unless the component is directional. `ICWResults.GetMinMaxDisplacement`, `ICWResults.GetMinMaxStrain` and `ICWResults.GetMinMaxFactorOfSafety2` follow the same pattern.
- Plots: `ICWResults.CreatePlot` with `swsPlotResultTypes_e` and a component, then read `GetMinMaxResultValues` on the plot, as the static-study plot examples do.
## Units and errors
- Simulation methods take explicit unit arguments (`swsUnit_e`, `swsLinearUnit_e`, `swsStrengthUnit_e`) instead of assuming SI; pass them by name and convert results accordingly ([units](correctness-rules.md#units)).
- Most calls return an integer error code or fill an ErrorCode out parameter, 0 meaning success; check every one before continuing ([errors and warnings](correctness-rules.md#errors-and-warnings)). VBA code can also read rich error text from the `Err` object.
## Sources
- `markdown/cworksapi/GettingStarted-swsimulationapi.md`
- `markdown/cworksapi/ReleaseNotes-swsimulationapi.md`
- `markdown/sldworksapiprogguide/Overview/Accessing_Add-ins.md`
- `markdown/cworksapi/Create_Plots_for_Static_Study_Example_CSharp.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy3.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddRestraint.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddForce3.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial2.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsAnalysisStudyType_e.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.md`
- `markdown/cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStressComponent_e.md`
