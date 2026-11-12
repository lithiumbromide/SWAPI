---
title: "ICWCompositeShellOptions Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html"
---

# ICWCompositeShellOptions Interface Members

The following tables list the members exposed by [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllPliesSameMaterial | Obsolete. Superseded by ICWCompositeShellOptions::AllPliesSameMaterial2 . |
| Property | AllPliesSameMaterial2 | Gets or sets whether the same material is applied to all plies. |
| Property | LengthUnit | Gets or sets the units of length. |
| Property | MappingType | Gets or sets the type of ply angle direction reference mapping. |
| Property | PlyRelativeAngle | Obsolete. Superseded by ICWCompositeShellOptions::PlyRelativeAngle2 . |
| Property | PlyRelativeAngle2 | Gets or sets whether ply angles are relative to the angle of ply 1. |
| Property | RotateZeroDegreeReference | Obsolete. Superseded by ICWCompositeShellOptions::RotateZeroDegreeReference2 . |
| Property | RotateZeroDegreeReference2 | Gets or sets whether to redefine the stripes on the composite shell so that the previous 90° ply angle now corresponds to the 0° ply angle. |
| Property | Sandwich | Obsolete. Superseded by ICWCompositeShellOptions::Sandwich2 . |
| Property | Sandwich2 | Gets or sets whether to use the sandwich composite formulation. |
| Property | Symmetric | Obsolete. Superseded by ICWCompositeShellOptions::Symmetric2 . |
| Property | Symmetric2 | Gets or sets whether the laminate layup is symmetric about the laminate mid-surface. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetMirrorOrientation | Obsolete. Superseded by ICWCompositeShellOptions::GetMirrorOrientation2 . |
| Method | GetMirrorOrientation2 | Gets the ply angle mirror orientation of this composite shell. |
| Method | GetPlanarMappingUVDirection | Gets the reference plane used to calculate the ply angle direction. |
| Method | GetPlyParameters | Gets the thickness, angle, and material for the specified ply. |
| Method | GetRotateOrientation | Obsolete. Superseded by ICWCompositeShellOptions::GetRotateOrientation2 . |
| Method | GetRotateOrientation2 | Gets whether to rotate the stripes by 90° along the surface of the ply of the specified face. |
| Method | GetTotalPlies | Gets the total number of plies in the composite laminate. |
| Method | SetMirrorOrientation | Obsolete. Superseded by ICWCompositeShellOptions::SetMirrorOrientation2 . |
| Method | SetMirrorOrientation2 | Sets the ply angle mirror orientation of this composite shell. |
| Method | SetPlanarMappingUVDirection | Sets the reference plane used to calculate the ply angle direction. |
| Method | SetPlyParameters | Obsolete. Superseded by ICWCompositeShellOptions::SetPlyParameters2 . |
| Method | SetPlyParameters2 | Sets the thickness, angle, and material for the specified ply. |
| Method | SetRotateOrientation | Obsolete. Superseded by ICWCompositeShellOptions::SetRotateOrientation2 . |
| Method | SetRotateOrientation2 | Sets whether to rotate the stripes by 90° along the surface of the ply of the specified face. |
| Method | SetTotalPlies | Sets the total number of plies in the composite laminate. |

[Top](#topBookmark)

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)
