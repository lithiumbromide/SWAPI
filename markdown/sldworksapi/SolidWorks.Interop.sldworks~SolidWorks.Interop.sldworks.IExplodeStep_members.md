---
title: "IExplodeStep Interface Members"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html"
---

# IExplodeStep Interface Members

The following tables list the members exposed by [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSpaceComponentsOnDrag | Gets or sets whether to automatically space a group of components equally along an axis as you drag them. |
| Property | DivergeDirection | Gets or sets the diverge direction entity for this radial explode step. |
| Property | DivergeFromAxis | Gets or sets whether to move components at an angle from the explode direction of this radial explode step. |
| Property | ExplodeDistance | Gets or sets the distance to move components in this regular or radial explode step. |
| Property | ExplodeStepType | Gets the type of this explode step. |
| Property | Name | Gets or sets the name of this explode step. |
| Property | ReverseRotationDirection | Gets or sets whether to reverse the direction of rotation of components in this regular explode step. |
| Property | ReverseTranslationDirection | Gets or sets whether to reverse the explode direction in this regular explode step. |
| Property | RotateAboutEachComponentOrigin | Gets or sets whether components rotate about their origins in this regular explode step. |
| Property | RotationAngle | Gets or sets the angle of component rotation in this regular or radial explode step. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetComponent | Gets the specified component in this explode step. |
| Method | GetComponentName | Gets the name of the specified component in this explode step. |
| Method | GetComponents | Gets the components of this explode step. |
| Method | GetComponentXform | Gets the transform of this explode step. |
| Method | GetExplodeDirection | Gets the explode direction (manipulator index and entity) for this explode step. |
| Method | GetNumOfComponents | Gets the number of components in this explode step. |
| Method | GetRotationAxis | Gets the rotation axis (manipulator index and entity) for this regular explode step. |
| Method | GetSpecificComponentXForm | Gets the transformation matrix of the specified component in this explode step. |
| Method | GetSubAssemblyExplodeSteps | Gets the explode steps of this subassembly explode step. |
| Method | IGetComponent | Gets the specified component in this explode step. |
| Method | IGetComponentXform | Gets the transform for this explode step. |
| Method | IsSubAssemblyRigid | Gets whether the subassembly is rigid or flexible. |
| Method | SetComponents | Specifies the components of this explode step. |
| Method | SetExplodeDirection | Sets the explode direction (manipulator index and entity) for this explode step. |
| Method | SetRotationAxis | Sets the rotation axis (manipulator index and entity) for this regular explode step. |

[Top](#topBookmark)

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAssemblyDoc::ShowExploded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded.html)
[IModelDoc2::IsExploded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded.html)
