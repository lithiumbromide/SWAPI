---
title: "IDatumOrigin Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html"
---

# IDatumOrigin Interface Members

The following tables list the members exposed by [IDatumOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Table | Gets the hole table associated with this datum origin. |
| Property | XLabel | Gets or sets the label for the X axis for this datum origin. |
| Property | YLabel | Gets or sets the label for the Y axis for this datum origin. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetAnnotation | Gets the IAnnotation object for this datum origin. |
| Method | GetAxisPoints | Obsolete. Superseded by IDatumOrigin::GetAxisPoints2 . |
| Method | GetAxisPoints2 | Gets the points that define the geometry of this datum origin. |
| Method | GetNext | Gets the next datum origin in the view. |
| Method | IGetAxisPoints | Obsolete. Superseded by IDatumOrigin::IGetAxisPoints2 . |
| Method | IGetAxisPoints2 | Gets the points that define the geometry of this datum origin. |
| Method | ISetAxisPoints | Sets the points that define the geometry of this datum origin. |
| Method | Reattach | Attaches the datum origin to a different entity. |
| Method | SetAxisPoints | Sets the points that define the geometry of this datum origin. |

[Top](#topBookmark)

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
