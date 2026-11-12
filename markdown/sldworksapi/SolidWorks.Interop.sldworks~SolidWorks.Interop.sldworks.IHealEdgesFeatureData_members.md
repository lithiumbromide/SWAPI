---
title: "IHealEdgesFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html"
---

# IHealEdgesFeatureData Interface Members

The following tables list the members exposed by [IHealEdgesFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AngularTolerance | Gets or sets the maximum angle between the edges to merge. |
| Property | EdgeLengthTolerance | Gets or sets the maximum length of the edges to merge. |
| Property | Faces | Gets the faces whose edges were healed or sets the faces whose edges you want healed. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe this heal edges feature. |
| Method | GetEdgeInformation | Gets the number of edges before healing and the number of edges after healing. |
| Method | GetFacesCount | Gets the number of faces for this heal edges feature. |
| Method | HealEdges | Merges the edges using the specified faces and tolerances. |
| Method | IGetFaces | Gets the faces whose edges to heal. |
| Method | ISetFaces | Gets the faces whose edges were healed. |
| Method | ReleaseSelectionAccess | Releases access to the selections that describe this heal edges feature. |

[Top](#topBookmark)

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
