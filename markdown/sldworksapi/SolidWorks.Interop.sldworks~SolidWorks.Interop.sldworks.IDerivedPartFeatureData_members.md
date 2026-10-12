---
title: "IDerivedPartFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html"
---

# IDerivedPartFeatureData Interface Members

The following tables list the members exposed by [IDerivedPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ImportAbsorbedSketches | Gets or sets whether to import absorbed sketches with the derived part feature. |
| Property | ImportAxis | Gets or sets whether to import the axis with the derived part feature. |
| Property | ImportCoordinateSystems | Gets or sets whether to import coordinate systems with the derived part feature. |
| Property | ImportCThread | Gets or sets whether to import cosmetic threads with the derived part feature. |
| Property | ImportCustomProperties | Gets or sets which custom properties to import with the derived part feature. |
| Property | ImportCutListProperties | Gets or sets whether to import cut list properties with the derived part feature. |
| Property | ImportHoleWizardData | Gets or sets whether to import Hole Wizard data with the derived part feature. |
| Property | ImportMaterial | Gets or sets whether to import material with the derived part feature. |
| Property | ImportModelDimensions | Gets or sets whether to import model dimensions with the derived part feature. |
| Property | ImportPlane | Gets or sets whether to import planes with the derived part feature. |
| Property | ImportSheetMetalInformation | Gets or sets how to import sheet metal information with the derived part feature. |
| Property | ImportSolidBodies | Gets or sets whether to import solid bodies with the derived part feature. |
| Property | ImportSurf | Gets or sets whether to import surface bodies with the derived part feature. |
| Property | ImportUnAbsorbedSketches | Gets or sets whether to import unabsorbed sketches with the derived part feature. |
| Property | PartConfiguration | Gets or sets the part configuration to use to create the derived part feature. |
| Property | PathName | Gets the path for the derived part feature. NOTE: This property is a get-only property. Set is not implemented . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections used to define this derived part feature. |
| Method | GetModelDoc | Gets the model document from which this part was derived (i.e., the base model document). |
| Method | GetMoveFeature | Gets the move/copy feature belonging to this derived part feature. |
| Method | IAccessSelections | Gains access to the selections used to define this derived part feature. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this derived part feature. |

[Top](#topBookmark)

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPartDoc::InsertPart2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart2.html)
[IFeature::ModifyDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html)
[IFeature::IModifyDefinition2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.html)
