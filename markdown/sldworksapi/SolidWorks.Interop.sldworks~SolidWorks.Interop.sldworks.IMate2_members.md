---
title: "IMate2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMate2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html"
---

# IMate2 Interface Members

The following tables list the members exposed by [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Alignment | Gets the type of alignment for this mate. |
| Property | CanBeFlipped | Gets whether this distance or angle mate can be flipped. |
| Property | DisplayDimension | Obsolete. Superseded by IMate2::DisplayDimension2 . |
| Property | DisplayDimension2 | Gets the specified display dimension for this mate. |
| Property | DistanceFirstArcCondition | Gets the the first arc condition of this distance mate between cylindrical components. |
| Property | DistanceSecondArcCondition | Gets the the second arc condition of this distance mate between cylindrical components. |
| Property | Flipped | Gets or sets whether to flip the distance or angle mate. |
| Property | HasLoadBearingFaces | Gets whether this mate has load bearing faces. |
| Property | HasTreatInterferenceAsShrinkFit | Gets whether interference in this mate is treated as shrink/press fit. |
| Property | IsLoadBearingFacesBonded | Get whether the load bearing faces of this mate are bonded. |
| Property | LockMagneticMate | Gets or sets whether to lock this magnetic mate. |
| Property | MateLoadReference | Gets the mate load reference associated with this mate. |
| Property | MaximumVariation | Gets the maximum variation, in meters or radians, for the dimension of this distance or angle mate. |
| Property | MinimumVariation | Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate. |
| Property | Type | Gets the type of mate. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ForceMisalignment | Forces a misaligned mate condition for this concentric mate. |
| Method | GetConcentricAlignmentType | Gets the alignment type of this mate. |
| Method | GetCurrentMisalignedDeviation | Gets the current misalignment deviation for the misaligned concentric mate. |
| Method | GetForce | Gets the magnitude and direction of the force applied to this mate. |
| Method | GetLinkedMate | Gets the linked mate of this concentric mate. |
| Method | GetMateEntityCount | Gets the number of entities for this mate. |
| Method | GetMaximumMisalignedDeviation | Gets the maximum allowed misalignment deviation for this misaligned concentric mate. |
| Method | GetSupplementalFaces | Gets the faces in this mate. |
| Method | GetTorque | Gets the angle and the axis of the torque applied to this mate. |
| Method | GetUseMisalignedDeviationDocumentProperty | Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate. |
| Method | IGetSupplementalFaces | Gets the faces in this mate. |
| Method | MateEntity | Gets an entity associated with a mate. |
| Method | RemoveMisalignment | Removes the misaligned mate condition of this concentric mate. |
| Method | SetConcentricAlignmentType | Sets the alignment type of this mate. |
| Method | SetForce | Sets the magnitude and direction of the force to apply to this mate. |
| Method | SetMaximumMisalignedDeviation | Sets the maximum allowed misalignment deviation for this misaligned concentric mate. |
| Method | SetTorque | Sets the angle and the axis of the torque to apply to this mate. |
| Method | SetUseMisalignedDeviationDocumentProperty | Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate. |

[Top](#topBookmark)

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)
[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
