# Assemblies
Traversing components, reading their states, renaming and replacing them, reading and creating mates, positioning components and checking interference.
## Contents
- [Traversal](#traversal)
- [Component data and states](#component-data-and-states)
- [Renaming and replacing](#renaming-and-replacing)
- [Mates](#mates)
- [Adding and positioning components](#adding-and-positioning-components)
- [Interference detection](#interference-detection)
## Traversal
- Hierarchical: `IConfigurationManager.ActiveConfiguration` (or `IModelDoc2.GetConfigurationByName`) once, `IConfiguration.GetRootComponent3(True)` once, then `IComponent2.GetChildren` recursively. `GetChildren` returns only the immediate children (null for parts), includes suppressed, hidden and lightweight components, and its result depends on the configuration each subassembly component references (`IComponent2.ReferencedConfiguration`).
- The root component is only a launching point for `GetChildren`; most other `IComponent2` members fail on it (`IComponent2.IsRoot` tells you which you have).
- Flat: `IAssemblyDoc.GetComponents(ToplevelOnly)` returns all components (False) or only top-level ones (True) in no defined order; `IAssemblyDoc.GetComponentCount` counts them. When order or parentage matters, walk the FeatureManager tree instead (`IModelDoc2.FirstFeature`, `IFeature.GetNextFeature`, `IFeature.GetTypeName2` returning `Reference` for components, `IFeature.GetSpecificFeature2` returning the `IComponent2`).
- Components are not returned in a stable order between calls, and the result changes with the active configuration ([configurations](correctness-rules.md#configurations)).
- Features of a component's part: get the component's model with `IComponent2.GetModelDoc2` and walk its tree, or walk `IComponent2.FirstFeature` for assembly-level context ([features-and-sketches.md](features-and-sketches.md#feature-traversal)).
## Component data and states
- Names: `IComponent2.Name2` is the instance name with its path in subassemblies (`subAssem1-2/Part1-1`); `IComponent2.GetPathName` is the file; `IComponent2.GetSelectByIDString` is the string for `SelectByID2` with type `COMPONENT`.
- States: `IComponent2.GetSuppression2` (`swComponentSuppressionState_e`), `IComponent2.Visible`, `IComponent2.IsVirtual`, `IComponent2.IsEnvelope`, `IComponent2.GetExcludeFromBOM2`. Resolve lightweight components before reading model data ([lightweight and suppressed components](correctness-rules.md#lightweight-and-suppressed-components)). Suppression in other configurations comes from `IConfigurationManager.GetConfigurationParams`, and subassemblies must be queried in their own documents.
- `IComponent2.GetModelDoc2` returns the saved state of the referenced file, not instance-level changes such as assembly features or material overrides; to read another configuration of that file, activate it there with `IModelDoc2.ShowConfiguration2`. Instance-level geometry comes from `IComponent2.GetBodies3`.
- Counting instances for a BOM: group `GetComponents(False)` by path and `ReferencedConfiguration`, skipping suppressed and excluded components; drawing BOM tables are covered in [drawings.md](drawings.md#bill-of-materials).
## Renaming and replacing
- Instance names: set `IComponent2.Name2` after turning the `swExtRefUpdateCompNames` toggle off with `ISldWorks.SetUserPreferenceToggle`, because the rename fails while that option is on, and restore the old value afterwards ([user preferences](correctness-rules.md#user-preferences)). The help also requires the component to be selected (`IComponent2.Select4`). SOLIDWORKS reserves some characters in names, for example `/` (subassembly path separator) and `@` (selection qualifier).
- Files: select the component and call `IModelDocExtension.RenameDocument(NewName)`; it returns `swRenameDocumentError_e` (virtual, lightweight, Toolbox, patterned and read-only components cannot be renamed). The new name lives in memory until saved; check `IModelDocExtension.HasRenamedDocuments`, update unopened referencing documents through `IRenamedDocumentReferences`, and save with references, otherwise `Save3` fails with `swFileSaveRequiresSavingReferences`.
- Replace: select top-level components and call `IAssemblyDoc.ReplaceComponents2(FileName, ConfigName, ReplaceAllInstance, UseConfigChoice, ReAttachMates)` with `swReplaceComponentsConfiguration_e`. Subassembly components must be replaced inside the opened subassembly, a component cannot be replaced by a file of the same name, and the call closes component files without saving them.
- Virtual components: `IAssemblyDoc.MakeIndependent` and `IModelDocExtension.IsVirtualComponent3` cover conversion and detection.
## Mates
- From the tree: find the feature whose `IFeature.GetTypeName2` is `MateGroup`, walk `IFeature.GetFirstSubFeature` and `IFeature.GetNextSubFeature`, and cast each `IFeature.GetSpecificFeature2` to `IMate2` (folders and other sub-features return other types, so test the cast).
- From a component: `IComponent2.GetMates` returns `IMate2` and `IMateInPlace` objects without iterating the whole mate folder, which is faster for long mate lists.
- `IMate2.Type` is `swMateType_e`; `IMate2.Alignment`, `IMate2.GetMateEntityCount` and `IMate2.MateEntity(i)` give the entities, and `IMateEntity2.ReferenceComponent` and `IMateEntity2.ReferenceType2` identify what each side references. The mate's name and suppression come from its feature (`IFeature.Name`, `IFeature.IsSuppressed2`).
- Mates of subassemblies live in each subassembly's own `MateGroup`; recurse into the subassembly documents when the user wants every mate.
- Creating: `IAssemblyDoc.CreateMateData(swMateType_e)` returns an `IMateFeatureData`; cast it to the mate-specific interface (`ICoincidentMateFeatureData`, `IDistanceMateFeatureData`, ...), set its properties or preselect the entities where the interface supports it, then call `IAssemblyDoc.CreateMate`. `IAssemblyDoc.AddMate5` is obsolete.
## Adding and positioning components
- `IAssemblyDoc.AddComponent5(CompName, ConfigOption, NewConfigName, UseConfigForPartReferences, ExistingConfigName, X, Y, Z)` needs the file already loaded in memory (open it with `ISldWorks.OpenDoc6` first, ideally invisible); X, Y, Z are meters relative to the component's bounding box, so position precisely afterwards. `IAssemblyDoc.AddComponents3` inserts many components with transforms in one call.
- Transforms: `IComponent2.Transform2` is relative to the root component and moves the component even against its mates; build an `IMathTransform` with `ISldWorks.GetMathUtility` and `IMathUtility.CreateTransform` from 16 doubles (3x3 rotation, translation in meters, scale, three unused). Afterwards rebuild only mates with `IModelDocExtension.Rebuild(swUpdateMates)` and call `IAssemblyDoc.UpdateBox`.
- Moves that must respect mates use the drag operator (`IAssemblyDoc.GetDragOperator`, `IDragOperator.EndDrag`), followed by `IModelDoc2.EditRebuild3`.
- `IComponent2.PresentationTransform` changes only the display (animations) and requires `IAssemblyDoc.EnablePresentation`.
- `IAssemblyDoc.EnableAssemblyRebuild` suspends rebuilds while adding many components ([batch performance](correctness-rules.md#batch-performance)).
## Interference detection
- `IAssemblyDoc.InterferenceDetectionManager` returns an `IInterferenceDetectionMgr`. Set its options (`TreatCoincidenceAsInterference`, `TreatSubAssembliesAsComponents`, `IncludeMultibodyPartInterferences`, `IgnoreHiddenBodies`), call `IInterferenceDetectionMgr.GetInterferences`, read each `IInterference.Components` and `IInterference.Volume`, then call `IInterferenceDetectionMgr.Done`.
- The older `IAssemblyDoc.ToolsCheckInterference2` works on an explicit component list.
## Sources
- `markdown/sldworksapiprogguide/Overview/Features_of_Components.md`
- `markdown/sldworksapiprogguide/Overview/Components,_Configurations,_and_Suppression_States.md`
- `markdown/sldworksapiprogguide/Overview/Work_with_Lightweight_Components.md`
- `markdown/sldworksapiprogguide/Overview/Presentation_Transforms.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMates.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMateData.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ArrayData.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.md`
- `markdown/sldworksapi/Get_Mates_and_Mate_Entities_Example_VB.md`
- `markdown/sldworksapi/Get_Mates_Example_VB.md`
- `markdown/sldworksapi/Rename_Components_and_Save_Assembly_Example_CSharp.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenameDocumentError_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRebuildOptions_e.md`
