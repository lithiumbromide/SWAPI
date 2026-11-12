---
title: "IRefPointFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html"
---

# IRefPointFeatureData Interface Members

The following tables list the members exposed by [IRefPointFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AlongCurveOption | Gets or sets whether to enable or disable the option to create the reference point along a curve or to create multiple reference points. |
| Property | Distance | Gets the distance at which the reference point was created or sets the distance at which to create the reference point. |
| Property | Selections | Gets the entities selected to create the reference point or sets the entities to create the reference point. |
| Property | Type | Gets or sets the type of reference point. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections used to create the reference point feature. |
| Method | GetSelectionsCount | Gets the number of entities selected to use to create the reference point. |
| Method | IAccessSelections | Accesses the selections used to create the reference point feature. |
| Method | IGetSelections | Gets the selected entities to use to create the reference points. |
| Method | ISetSelections | Sets the number of entities to use to create the reference points. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this reference point feature. |

[Top](#topBookmark)

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::IInsertReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertReferencePoint.html)
[IFeatureManager::InsertReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertReferencePoint.html)
[IRefPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)
