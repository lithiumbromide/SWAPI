---
title: "ICWBeamBody Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html"
---

# ICWBeamBody Interface Members

The following tables list the members exposed by [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BeamBodyName | Gets the name of the beam. |
| Property | BeamDistForMaxShearStress | Gets or sets the maximum distance from the shear center to the furthest point on the cross-section of this beam body. |
| Property | BeamEnd1ConnectionType | Gets or sets the End1 connection for this beam. |
| Property | BeamEnd2ConnectionType | Gets or sets the End2 connection for this beam. |
| Property | BeamShearY | Gets or sets the shear factor in direction 1 of the cross-section of this beam body. |
| Property | BeamShearZ | Gets or sets the shear factor in direction 2 of the cross-section of this beam body. |
| Property | BeamTorsionalConstant | Gets or sets the torsional stiffness constant for the cross-section of this beam body. |
| Property | BeamTorsionalConstantUnit | Gets or sets the units of length for cross-section calculations of this beam body. |
| Property | BeamType | Gets or sets the type of beam. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | BeamBeginEdit | Begins editing of a beam. |
| Method | BeamEndEdit | Ends editing of a beam. |
| Method | ConvertToSolidBody | Treats a beam as a solid body. |
| Method | GetBeamBodyMaterial | Gets the material applied to the beam for analysis. |
| Method | GetDefaultMaterial | Gets the CAD material of the beam. |
| Method | GetManualEnd1ConnectionType | Obsolete. Superseded by ICWBeamBody::GetManualEnd1ConnectionType2 . |
| Method | GetManualEnd1ConnectionType2 | Gets whether manual forces and moments are known to be zero for the End1 connection of the beam. |
| Method | GetManualEnd2ConnectionType | Obsolete. Superseded by ICWBeamBody::GetManualEnd2ConnectionType2 . |
| Method | GetManualEnd2ConnectionType2 | Gets whether manual forces and moments are known to be zero for End2 connection of the beam. |
| Method | SetBeamBodyMaterial | Sets the material for the beam for analysis. |
| Method | SetFavMaterial | Obsolete. Superseded by ICWBeamBody::SetFavMaterial2 . |
| Method | SetFavMaterial2 | Applies the specified material from the material favorites list. |
| Method | SetLibraryMaterial | Obsolete. Superseded by ICWBeamBody::SetLibraryMaterial2 . |
| Method | SetLibraryMaterial2 | Sets the material library and material name for the beam. |
| Method | SetManualEnd1ConnectionType | Obsolete. Superseded by ICWBeamBody::SetManualEnd1ConnectionType2 . |
| Method | SetManualEnd1ConnectionType2 | Sets whether manual forces and moments are known to be zero for End1 connection of the beam. |
| Method | SetManualEnd2ConnectionType | Obsolete. Superseded by ICWBeamBody::SetManualEnd2ConnectionType2 . |
| Method | SetManualEnd2ConnectionType2 | Sets whether manual forces and moments are known to be zero for End2 connection of the beam. |

[Top](#topBookmark)

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
