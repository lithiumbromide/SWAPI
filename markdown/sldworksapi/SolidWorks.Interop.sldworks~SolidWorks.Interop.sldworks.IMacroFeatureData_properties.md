---
title: "IMacroFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_properties.html"
---

# IMacroFeatureData Interface Properties

For a list of all members of this type, see [IMacroFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CurrentConfiguration | Gets the macro feature configuration being rebuilt. |
| Property | EditBodies | Gets or sets the bodies to be modified by this macro feature. |
| Property | EditBody | Obsolete. Superseded by IMacroFeatureData::IGetEditBodies , IMacroFeatureData::ISetEditBodies , and IMacroFeatureData::EditBodies . |
| Property | EnableMultiBodyConsume | Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature. |
| Property | FeatureTransform | Gets and sets the macro feature transform. |
| Property | IconFiles | Gets or sets the file names for the icons for this macro feature. |
| Property | MacroFileEmbedded | Gets whether the macro file is embedded ini the model with the macro feature. |
| Property | MacroFileName | Gets or sets the path and file name for the macro for the macro feature. |
| Property | ModuleName | Gets or sets the name of a module in the macro for this macro feature. |
| Property | Parents | Gets or sets the parent features for this macro feature. |
| Property | PatternTransform | Gets the pattern transform. |
| Property | ProcedureName | Gets or sets a name of the procedure in the macro for this macro feature. |
| Property | PropertyManagerHandleMacroFileName | Gets or sets the path and file name for the macro file from or to the PropertyManager handle for this macro feature. |
| Property | PropertyManagerHandleModuleName | Gets or sets the name of the module in the macro file from or to the PropertyManager handle. |
| Property | PropertyManagerHandleProcedureName | Gets or sets the name of the procedure in the macro file from or to the PropertyManager handle. |
| Property | Provider | Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files. |
| Property | SecurityHandleMacroFileName | Gets or sets the name of the procedure in the macro file from or to the security handle. |
| Property | SecurityHandleModuleName | Gets and sets the name of the module in the macro file from or to the security handle. |
| Property | SecurityHandleProcedureName | Gets or sets the name of the procedure in the macro file from or to the security handle. |

[Top](#topBookmark)

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::IInsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html)
[IFeatureManager::InsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html)
