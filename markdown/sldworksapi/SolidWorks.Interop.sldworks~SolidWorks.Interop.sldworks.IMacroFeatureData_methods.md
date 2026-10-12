---
title: "IMacroFeatureData Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_methods.html"
---

# IMacroFeatureData Interface Methods

For a list of all members of this type, see [IMacroFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections associated with this macro feature. |
| Method | EmbedMacroFile | Sets whether to embed the macro file in the model with the macro feature. |
| Method | GetBaseName | Gets the name of the base feature for this macro feature. |
| Method | GetDisplayDimensionCount | Gets the number of display dimensions for this macro feature. |
| Method | GetDisplayDimensions | Gets the display dimensions for this macro feature. |
| Method | GetDoubleByName | Gets a double value by parameter name. |
| Method | GetEdgeIdType | Gets the ID type of the specified edge for the macro feature. |
| Method | GetEdgeUserId | Gets the user-defined IDs for the specified edge for the macro feature. |
| Method | GetEditBodiesCount | Gets the number of bodies to be modified by this macro feature. |
| Method | GetEditTargetTransform | Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component. |
| Method | GetEntitiesNeedUserId | Gets a list of faces and edges that need be assigned user IDs for the macro feature. |
| Method | GetEntitiesNeedUserIdCount | Gets the number of faces and edges that need to be assigned user IDs for the macro feature. |
| Method | GetFaceIdType | Gets the ID type from the face for the macro feature. |
| Method | GetFaceUserId | Gets the user-defined IDs for the specified face. |
| Method | GetIconFileCount | Gets the number of the files for the icons for this macro feature. |
| Method | GetIntegerByName | Gets an integer value by parameter name. |
| Method | GetModuleCount | Gets the number of modules for the macro feature. |
| Method | GetModuleNames | Gets the names of the modules in the macro for the macro feature. |
| Method | GetParameterCount | Gets the number of user-defined parameters. |
| Method | GetParameters | Gets the user-defined parameters. |
| Method | GetParentsCount | Gets the number of parent features for this macro feature. |
| Method | GetProcedureCount | Gets the number of procedures in the specified module in the macro for this macro feature. |
| Method | GetProcedureNames | Gets the names of the procedures in the specified module for the macro for the macro feature. |
| Method | GetProgId | Gets the version-independent program ID that is valid for this COM feature. |
| Method | GetPropertyManagerHandleModuleCount | Gets the number of modules in the macro from the PropertyManager handle for the macro feature. |
| Method | GetPropertyManagerHandleModuleNames | Gets the names of the modules in the macro from the PropertyManager handle for the macro feature. |
| Method | GetPropertyManagerHandleProcedureCount | Gets the number of procedures in the specified module in the macro from the PropertyManager handle for this macro feature. |
| Method | GetPropertyManagerHandleProcedureNames | Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature. |
| Method | GetSelectionCount | Gets the number of selected objects for the macro feature. |
| Method | GetSelections | Obsolete. Superseded by IMacroFeatureData::GetSelections3 . |
| Method | GetSelections2 | Obsolete. Superseded by IMacroFeatureData::GetSelections3 . |
| Method | GetSelections3 | Gets the selected objects for the macro feature. |
| Method | GetStringByName | Gets a string value by the name of the parameter for the macro feature. |
| Method | IAccessSelections | Gains access to the selections associated with this macro feature. |
| Method | IAddDisplayDimensions | Adds the specified display dimensions to this macro feature. |
| Method | IGetDisplayDimensions | Gets the display dimensions for this macro feature. |
| Method | IGetEditBodies | Gets the bodies to be modified by this macro feature. |
| Method | IGetEntitiesNeedUserId | Gets a list of faces and edges that need be assigned user IDs for the macro feature. |
| Method | IGetIconFiles | Gets the file names for the icons for this macro feature. |
| Method | IGetModuleNames | Gets the names of the modules in the macro for the macro feature. |
| Method | IGetParameters | Gets the user-defined parameters. |
| Method | IGetParents | Gets the parent features of this macro feature. |
| Method | IGetProcedureNames | Gets the names of the procedures in the specified module in the macro for the macro feature. |
| Method | IGetPropertyManagerHandleModuleNames | Gets the names of the modules in the macro from the PropertyManager handle for the macro feature. |
| Method | IGetPropertyManagerHandleProcedureNames | Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature. |
| Method | IGetSelections | Obsolete. Superseded by IMacroFeatureData::IGetSelections3 . |
| Method | IGetSelections2 | Obsolete. Superseded by IMacroFeatureData::IGetSelections3 . |
| Method | IGetSelections3 | Gets the selected objects for the macro feature. |
| Method | IsCOMFeature | Gets whether the feature is a COM feature. |
| Method | ISetEditBodies | Sets the bodies to be modified by this macro feature. |
| Method | ISetIconFiles | Sets the file names for the icons for this macro feature. |
| Method | ISetParameters | Sets the user-defined parameters. |
| Method | ISetParents | Sets the parent features for this macro feature. |
| Method | ISetSelections | Obsolete. Superseded by IMacroFeatureData::ISetSelections2 . |
| Method | ISetSelections2 | Sets the selected objects for the macro feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections associated with this macro feature. |
| Method | SetDoubleByName | Sets a double value by parameter name for the macro feature. |
| Method | SetEdgeUserId | Sets the user-defined IDs for the specified edge for the macro feature. |
| Method | SetFaceUserId | Sets user-defined IDs for the face for the macro feature. |
| Method | SetIntegerByName | Sets an integer value by parameter name. |
| Method | SetParameters | Sets the user-defined parameters. |
| Method | SetProgId | Sets the version-independent program ID that is valid for this COM feature. |
| Method | SetSelections | Obsolete. Superseded by IMacroFeatureData::SetSelections2 . |
| Method | SetSelections2 | Sets the selected objects for the macro feature. |
| Method | SetStringByName | Sets a string value by parameter name. |

[Top](#topBookmark)

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::IInsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html)
[IFeatureManager::InsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html)
