---
title: "IAnnotationView Interface Members"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html"
---

# IAnnotationView Interface Members

The following tables list the members exposed by [IAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Always2D | Gets whether to display annotations in 2D or 3D. |
| Property | AngleMadeWithViewHorizontal | Gets the angle used to make the annotation view horizontal. |
| Property | AnnotationCount | Gets the number of annotations in this annotation view. |
| Property | Annotations | Obsolete. Superseded by IAnnotationView::GetAnnotations2 . |
| Property | FlatPatternView | Gets whether this annotation view is a flat-pattern view. |
| Property | UnassignedView | Gets whether this annotation view is assigned to a 3D View. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Activate | Activates this annotation view. |
| Method | ActivateAndReorient | Activates and reorients this annotation view. |
| Method | GetAnnotations2 | Gets the annotations in this annotation view. |
| Method | GetViewRotation | Gets the rotation matrix of the annotation view relative to the X-Y plane of the model. |
| Method | Hide | Hides the annotations in an annotation view that is not activated. |
| Method | IGetAnnotations | Obsolete. Superseded by IAnnotationView::GetAnnotations2 . |
| Method | IGetViewRotation | Gets the rotation matrix of the annotation view relative to the X-Y plane of the model. |
| Method | IsShown | Gets whether the annotations in this annotation view are shown. |
| Method | MoveAnnotations | Moves the specified annotations to this annotation view. |
| Method | Orient | Orients this annotation view. |
| Method | Show | Shows the annotations in an annotation view that is not activated. |

[Top](#topBookmark)

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
