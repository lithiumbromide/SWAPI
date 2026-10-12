---
title: "IModelDoc2 Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_properties.html"
---

# IModelDoc2 Interface Properties

For a list of all members of this type, see [IModelDoc2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ActiveView | Gets the current active model view in read-only mode. NOTE: This property is a get-only property. Set is not implemented . |
| Property | ConfigurationManager | Gets the IConfigurationManager object, which allows access to a configuration in a model. |
| Property | CustomInfo | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Property | CustomInfo2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Property | Extension | Gets the IModelDocExtension object, which also allows access to the model document. |
| Property | FeatureManager | Gets the IFeatureManager object, which allows access to the FeatureManager design tree. |
| Property | FeatureManagerSplitterPosition | Splits the FeatureManager design tree and gets or sets the location of the split bar in the FeatureManager design tree panel. |
| Property | IActiveView | Gets the current active model view in read-only mode. NOTE: This property is a get-only property. Set is not implemented . |
| Property | ILightSourcePropertyValues | Gets and sets the light source property values. |
| Property | IMaterialPropertyValues | Gets or sets a material's properties in the active configuration. |
| Property | IPageSetup | Gets the page setup for this document. |
| Property | ISelectionManager | Gets the ISelectionMgr object for this document, which makes the currently selected object available. |
| Property | LargeAssemblyMode | Gets or sets Large Assembly Mode for this document. |
| Property | LengthUnit | Gets and sets the same LengthUnit value used by IModelDoc2::GetUnits , IModelDoc2::IGetUnits , and IModelDoc2::SetUnits . |
| Property | LightSourcePropertyValues | Gets and sets the light source property values. |
| Property | LightSourceUserName | Gets or sets the light source name that is displayed in the SOLIDWORKS Design user interface. |
| Property | MaterialIdName | Obsolete. Superseded by IPartDoc::GetMaterialPropertyName2 and IPartDoc::SetMaterialPropertyName2 . |
| Property | MaterialPropertyValues | Gets or sets a material's properties in the active configuration. |
| Property | MaterialUserName | Gets or sets the material name. |
| Property | ModelViewManager | Gets the IModelViewManager object, which allows access to the model view. |
| Property | PageSetup | Gets the page setup for this document. |
| Property | Printer | Gets or sets the default printer for this document. |
| Property | PrintSetup | Obsolete. See IModelDo2::SetUserPreferenceDoubleValue , IModelDoc2::SetUserPreferenceIntegerValue , and IModelDoc2::SetUserPreferenceToggle . |
| Property | SceneBkgImageFileName | Controls the image filename used as the current background picture. |
| Property | SceneName | Gets and sets the name of the scene. |
| Property | SceneUserName | Gets and sets the user name of the scene. |
| Property | SelectionManager | Gets the ISelectionMgr object for this document, which makes the currently selected object available. NOTE: This property is a get-only property. Set is not implemented . |
| Property | ShowFeatureErrorDialog | Gets or sets whether to display the feature error dialog. |
| Property | SketchManager | Gets the sketch manager, which allows access to sketch-creation routines. |
| Property | SummaryInfo | Gets or sets file summary information for the SOLIDWORKS document. |
| Property | Visible | Gets or sets the visibility of the active document. |

[Top](#topBookmark)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
