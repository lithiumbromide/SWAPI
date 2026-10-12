---
title: "IDomeFeatureData2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html"
---

# IDomeFeatureData2 Interface Members

The following tables list the members exposed by [IDomeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ConstraintPointOrSketch | Gets or sets the constraining point or sketch for a dome feature. |
| Property | Direction | Gets or sets the direction of the dome feature. |
| Property | Elliptical | Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii. |
| Property | Face | Obsolete. Superseded by IDomeFeatureData2::Faces . |
| Property | Faces | Gets or sets the planar or non-planar faces of this dome feature. |
| Property | Height | Gets or sets the height of the dome. |
| Property | IFace | Obsolete. Superseded by IDomeFeatureData2::Faces . |
| Property | ReverseDir | Gets or sets whether this dome is convex or concave. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define the dome. |
| Method | GetFaceCount | Gets the number of planar and non-planar faces of this dome feature. |
| Method | IAccessSelections | Gains access to selections used to define the dome. |
| Method | IGetFaces | Gets the planar or non-planar faces of this dome feature. |
| Method | ISetFaces | Sets the planar or non-planar faces of this dome feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define this dome feature. |

[Top](#topBookmark)

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertDome Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDome.html)
