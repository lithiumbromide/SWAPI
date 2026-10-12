---
title: "IShellFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html"
---

# IShellFeatureData Interface Members

The following tables list the members exposed by [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Direction | Gets and sets the direction of this shell feature. |
| Property | FacesRemoved | Gets the faces removed and sets the faces to remove in this shell feature. |
| Property | FacesRemovedCount | Gets the number of faces removed in this shell feature. |
| Property | MultipleThicknessFaces | Gets and sets the multiple-thickness faces in this shell feature. |
| Property | Thickness | Gets and sets the overall thickness of the shell feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this shell feature. |
| Method | GetMultipleThicknessAtIndex | Gets the thickness of the shell at the specified index in this shell feature. |
| Method | GetMultipleThicknessFacesCount | Gets the number of faces with multiple thickness in this shell feature. |
| Method | IAccessSelections | Gains access to the selections that define this shell feature. |
| Method | IGetFacesRemoved | Gets the faces removed in this shell feature. |
| Method | IGetMultipleThicknessFaces | Gets the multiple-thickness faces in this shell feature. |
| Method | ISetFacesRemoved | Sets the faces to remove in this shell feature. |
| Method | ISetMultipleThicknessFaces | Sets the multiple-thickness faces in this shell feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define this shell feature. |
| Method | SetMultipleThicknessAtIndex | Sets the thickness of the shell at this index in this shell feature. |

[Top](#topBookmark)

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertFeatureShell Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShell.html)
