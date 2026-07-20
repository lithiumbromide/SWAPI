---
title: "ILibraryFormToolFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html"
---

# ILibraryFormToolFeatureData Interface Members

The following tables list the members exposed by[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | FormToolConfiguration | Gets or sets the configuration of this forming tool's part to insert. |
| Property | FormToolPath | Gets or sets the pathname of this forming tool's part in the Design Library. |
| Property | LinkToFormTool | Gets or sets whether to link this forming tool to its part in the Design Library. |
| Property | OverrideSettings | Gets whether the document settings are overridden when displaying this forming tool in its flat pattern. |
| Property | PickPoint | Gets the pickpoint where this forming tool is inserted. |
| Property | PlacementFace | Gets the placement face where this forming tool is inserted. |
| Property | RotationAngle | Gets or sets the rotation angle of this forming tool. |
| Property | ShowCenter | Gets whether to display the center mark where this forming tool is located in the flat pattern. |
| Property | ShowProfile | Gets whether to display the placement sketch of this forming tool when the part is flattened. |
| Property | ShowPunch | Gets whether to display the cut of this forming tool when the part is flattened. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections that define this library forming tool feature. |
| Method | GetPunchID | Gets the punch ID assigned to the Design Library forming tool. |
| Method | OverrideDocumentSettings | Specifies the flat pattern visibility options for this forming tool feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this library forming tool feature. |
| Method | SetPlacementFace | Specifies the face and pickpoint where the forming tool is inserted. |

[Top](#topBookmark)

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IFeatureManager::CreateFormTool2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool2.html)

[IView::InsertPunchTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable.html)
