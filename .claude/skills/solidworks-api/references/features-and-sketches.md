# Features and sketches
Traversing the FeatureManager tree, reading and editing feature definitions, creating features and sketches, changing dimensions and equations, and writing macro features.
## Contents
- [Feature traversal](#feature-traversal)
- [Feature data objects](#feature-data-objects)
- [Creating features](#creating-features)
- [Sketches](#sketches)
- [Dimensions and equations](#dimensions-and-equations)
- [Macro features](#macro-features)
## Feature traversal
- Start with `IModelDoc2.FirstFeature` (parts, assemblies and drawings; it returns suppressed features too) and continue with `IFeature.GetNextFeature`; children such as sketches under an extrusion or mates under the mate folder come from `IFeature.GetFirstSubFeature` and `IFeature.GetNextSubFeature`. `IFeatureManager.GetFeatures(ToplevelOnly)` returns them as an array.
- Identify features by `IFeature.GetTypeName2` (for example `ProfileFeature` for sketches, `RefPlane`, `Boss`, `Cut`, `MateGroup`, `Reference` for components, `BomFeat`, `FlatPattern`, `CutListFolder`, `SolidBodyFolder`), never by their default names, because users rename and reorder features and the definition order differs from the displayed order ([persistent references](correctness-rules.md#persistent-references)).
- `IFeature.GetSpecificFeature2` returns the specific object (`ISketch`, `IRefPlane`, `IComponent2`, `IMate2`, `IBomFeature`, `IBodyFolder`), while `IFeature.GetDefinition` returns the feature data object used for editing. The type table in the `IFeature.GetTypeName2` topic maps each type name to its interface.
- Name and state: `IFeature.Name` (settable), `IFeature.IsSuppressed2(swInConfigurationOpts_e, ConfigNames)`, `IFeature.SetSuppression2`, `IFeature.GetErrorCode2`; relations with `IFeature.GetParents` and `IFeature.GetChildren`; faces with `IFeature.GetFaces`.
- `IPartDoc.FeatureByName` finds a feature by name when the user supplies it; `IFeature.GetNameForSelection` gives the name and type for `SelectByID2` ([selection](correctness-rules.md#selection)).
## Feature data objects
- Edit sequence: `IFeature.GetDefinition` returns an object whose interface ends in `FeatureData` or `FeatureData2` (`IExtrudeFeatureData2`, `ISimpleFilletFeatureData2`, `ISweepFeatureData`, `IWizardHoleFeatureData2`); check it for null because not every feature type has one.
- Call the data object's `AccessSelections(TopDoc, Component)` (`IExtrudeFeatureData2.AccessSelections` and equivalents) before reading or changing selections, which rolls the model back to that feature.
- Change properties, then call `IFeature.ModifyDefinition(Data, TopDoc, Component)`, which releases the selection access automatically. If you change nothing, call the data object's `ReleaseSelectionAccess` (`IExtrudeFeatureData2.ReleaseSelectionAccess`) instead, or the model stays rolled back.
- In a part, TopDoc is the part and Component is Nothing; in an assembly, TopDoc is the assembly and Component is the component that owns the feature, and the assembly is left in Edit Part mode (return with `IAssemblyDoc.EditAssembly`).
- `ModifyDefinition` can return True and still produce a rebuild error: check `IFeature.GetErrorCode2`, and repair with `IModelDoc2.ForceRebuild3` or valid data ([null checks and return values](correctness-rules.md#null-checks-and-return-values)).
- Values on data objects are in meters and radians ([units](correctness-rules.md#units)).
## Creating features
- Classic creators take long positional argument lists after you select the sketch or entities: `IFeatureManager.FeatureExtrusion3`, `IFeatureManager.FeatureCut4`, `IFeatureManager.FeatureRevolve2`, `IFeatureManager.FeatureFillet3`, `IFeatureManager.InsertRefPlane`. Look each one up with `sig` and `enum` instead of copying old macros, because the suffixes change between releases ([current members only](correctness-rules.md#current-members-only)).
- Definition-based creators: `IFeatureManager.CreateDefinition(swFeatureNameID_e)` returns a feature data object initialized with defaults (patterns, sweeps, bounding box, mirror components, sheet metal edge flanges, tab and slot, library features); set its properties, select references, then call `IFeatureManager.CreateFeature(data)`.
- Patterns: `swFmLPattern` (`ILinearPatternFeatureData`), `swFmCirPattern` (`ICircularPatternFeatureData`), `swFmCurvePattern`, `swFmSketchPattern`, `swFmTablePattern`, `swFmFillPattern`, `swFmDimPattern`, and `swFmLocal*` variants for component patterns in assemblies.
- Sweeps: select the profile, path, guide curves and optional direction vector with the marks listed under [selection](correctness-rules.md#selection) (`IModelDocExtension.SelectByRay` picks reliably), create the data with `swFmSweep` or `swFmSweepCut`, and with a direction vector set `ISweepFeatureData.PathAlignmentType` to `swTangencyDirectionVector` and `ISweepFeatureData.TwistControlType` to `swTwistControlFollowPath`. Thin sweeps must be configured before creation.
- Hole Wizard: create `IWizardHoleFeatureData2` with `CreateDefinition`, call `IWizardHoleFeatureData2.InitializeHole`, adjust properties, select the placement face or sketch points, then `CreateFeature`; or reuse the definition of an existing hole.
- Library features: `CreateDefinition(swFmLibraryFeature)`, `ILibraryFeatureData.Initialize(path)` (opens the last active configuration), `ILibraryFeatureData.GetReferences3` for the required references, select them, then `CreateFeature`.
## Sketches
- Open a sketch on a selected plane or face with `ISketchManager.InsertSketch(True)` and close it with the same call; `ISketchManager.ActiveSketch` returns the open `ISketch`. `IModelDoc2.InsertSketch2` is obsolete.
- Create entities with `ISketchManager.CreateLine`, `ISketchManager.CreateCircleByRadius`, `ISketchManager.CreateArc`, `ISketchManager.CreateCornerRectangle`, `ISketchManager.CreateCenterLine`, `ISketchManager.CreatePoint` and `ISketchManager.CreateSpline3`; coordinates are meters in sketch space.
- Set `ISketchManager.AddToDB` to True to bypass snapping and inference while creating entities, and `ISketchManager.DisplayWhenAdded` to False to skip redraws (it requires AddToDB). Reset both when done, because they persist after your program ends; some entity creation cannot be undone while AddToDB is True. Add relations afterwards with `ISketch.ConstrainAll` or `IModelDoc2.SketchAddConstraints`.
- Read sketch geometry with `ISketch.GetSketchSegments` and `ISketchSegment.GetType`; `ISketchSegment.ConstructionGeometry` marks construction lines.
- Splines: `ISketchManager.CreateSpline3` interpolates through points; the `ICurve` parameter methods return the b-spline or polynomial forms described in the Splines topic.
## Dimensions and equations
- Get a dimension by full name with `IModelDoc2.Parameter("D1@Sketch1")` (or `"D1@Boss-Extrude1"`), or without the feature suffix through `IFeature.Parameter`; names containing `@` or `.` in part or feature names can make `Parameter` fail. Walk a feature's dimensions with `IFeature.GetFirstDisplayDimension`, `IFeature.GetNextDisplayDimension` and `IDisplayDimension.GetDimension2`.
- Set values with `IDimension.SetSystemValue3(value, swSetValueInConfiguration_e, ConfigNames)` and read with `IDimension.GetSystemValue3` ([units](correctness-rules.md#units)). `SetSystemValue3` also changes read-only dimensions (`IDimension.ReadOnly`). Rebuild with `IModelDoc2.EditRebuild3` afterwards.
- Equations: `IModelDoc2.GetEquationMgr` returns `IEquationMgr`; add with `IEquationMgr.Add3(Index, Equation, Solve, WhichConfigurations, ConfigNames)`, read with `IEquationMgr.Equation(i)`, `IEquationMgr.Value(i)` and `IEquationMgr.GetCount`, change with `IEquationMgr.SetEquationAndConfigurationOption`, delete with `IEquationMgr.Delete`, and recompute with `IEquationMgr.EvaluateAll`.
## Macro features
- A macro feature is a feature whose rebuild is your code. Insert it with `IFeatureManager.InsertMacroFeature3`, passing the base name, either a VBA macro file and the names of its functions or the ProgID of a COM server, parameter names, types and values, dimensions, edit bodies and `swMacroFeatureOptions_e` flags. Selections active at insertion are stored with the feature.
- VBA macro features live in a `.swp`; their functions start with `swm` and take three Variant arguments (app, part, feature). Rebuild and edit definition functions are required, security is optional. SOLIDWORKS .NET (VSTA) macros cannot define macro features, and `swMacroFeatureEmbedMacroFile` is not supported from .NET.
- COM macro features implement `ISwComFeature` (`ISwComFeature.Regenerate`, `ISwComFeature.Edit`, `ISwComFeature.Security`, all required) in a `ComVisible` class registered under the ProgID passed to `InsertMacroFeature3`. Strong-name and version COM servers when several major SOLIDWORKS versions share a machine.
- Rebuild functions read parameters and selections from `IMacroFeatureData`, must not create other features or interact with the user, and return True, False or an error string; multibody output uses `IMacroFeatureData.EnableMultiBodyConsume`.
- Edit definition functions call `IMacroFeatureData.AccessSelections`, collect input (a PropertyManager page works well), write the data back and call `IFeature.ModifyDefinition`. Configuration-specific dimension changes belong here (`IDimension.SetSystemValue3`), never in the rebuild function.
- Security functions return `swMacroFeatureSecurityOptions_e` flags; calling `IFeature.GetDefinition` there recurses, so guard it with a static flag.
## Sources
- `markdown/sldworksapiprogguide/Miscellaneous/Accessing_Selections_that_Define_Features.md`
- `markdown/sldworksapiprogguide/Miscellaneous/IFeatureInterfaceInheritance.md`
- `markdown/sldworksapiprogguide/Overview/Pattern_Features_and_their_Feature_Data_Objects.md`
- `markdown/sldworksapiprogguide/Overview/Sweep_Features_and_SweepFeatureData_Objects.md`
- `markdown/sldworksapiprogguide/Overview/Hole_Wizard_Features_and_WizardHoleFeatureData2_Objects.md`
- `markdown/sldworksapiprogguide/Overview/Library_Features_and_LibraryFeatureData_Objects.md`
- `markdown/sldworksapiprogguide/Overview/Splines.md`
- `markdown/sldworksapiprogguide/Macro_Features/Overview_of_Macro_Features.md`
- `markdown/sldworksapiprogguide/Macro_Features/Inserting_Macro_Features.md`
- `markdown/sldworksapiprogguide/Macro_Features/Rebuild_Function.md`
- `markdown/sldworksapiprogguide/Macro_Features/Edit_Definition_Function.md`
- `markdown/sldworksapiprogguide/Macro_Features/Security_Function.md`
- `markdown/sldworksapiprogguide/Macro_Features/Exposed_COM_DLL_or_Executable.md`
- `markdown/sldworksapiprogguide/Macro_Features/VBA_Macro_Files.md`
- `markdown/sldworksapiprogguide/Macro_Features/Macro_Features_and_Strong_Name_Versioning.md`
- `markdown/sldworksapiprogguide/Macro_Features/Macro_Features,_Configurations,_and_Dimensions.md`
- `markdown/sldworksapiprogguide/Macro_Features/MacroFeatureData_Interface.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMacroFeatureOptions_e.md`
