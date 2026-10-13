---
title: "ICWForce Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html"
---

# ICWForce Interface Members

The following tables list the members exposed by [ICWForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Equation | Gets or sets the equation describing this force of nonuniform distribution. |
| Property | EquationAngularUnit | Gets or sets the angular units for the cylindrical or spherical coordinate system of this force of nonuniform distribution. |
| Property | EquationCoordinateSystemType | Gets or sets the type of coordinate system used to define this force of nonuniform distribution. |
| Property | EquationLinearUnit | Gets or sets the linear units for the Cartesian, cylindrical, or spherical coordinate system of this force of nonuniform distribution. |
| Property | ForceType | Gets or sets the force type. |
| Property | IncludeNonUniformDistribution | Obsolete. Superseded by ICWForce::IncludeNonUniformDistribution2 . |
| Property | IncludeNonUniformDistribution2 | Gets or sets whether to use a nonuniform distribution of this force. |
| Property | NormalForceOrTorqueValue | Gets or sets the normal or torque value of this force. |
| Property | PhaseAngle | Gets or sets the phase angle of the force in a harmonic analysis of a linear dynamic study. |
| Property | PhaseAngleUnit | Gets or sets the units of phase angle of the force in a harmonic analysis of a linear dynamic study. |
| Property | Unit | Gets or sets the units of force. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ForceBeginEdit | Starts editing a force. |
| Method | ForceEndEdit | Ends editing a force. |
| Method | GetCoordinateSystem | Gets the coordinate system used for defining a force of nonuniform distribution. |
| Method | GetForceComponentValues | Obsolete. Superseded by ICWForce::GetForceComponentValues2 . |
| Method | GetForceComponentValues2 | Gets the force component values. |
| Method | GetMomentComponentValues | Obsolete. Superseded by ICWForce::GetMomentComponentValues2 . |
| Method | GetMomentComponentValues2 | Gets the moment values. |
| Method | GetNonUniformData | Obsolete. Superseded by ICWForce::Equation . |
| Method | GetTimeCurve | Gets the time curve data for this time-dependent force in a dynamic study. |
| Method | InsertEntity | Adds an entity to the set of entities to which to apply this force or torque. |
| Method | RemoveEntity | Removes an entity at the specified index. |
| Method | SetCoordinateSystem | Sets the coordinate system used for defining a force of nonuniform distribution. |
| Method | SetForceComponentValues | Obsolete. Superseded by ICWForce::SetForceComponentValues2 . |
| Method | SetForceComponentValues2 | Sets the force component values. |
| Method | SetMomentComponentValues | Obsolete. Superseded by ICWForce::SetMomentComponentValues2 . |
| Method | SetMomentComponentValues2 | Sets the moment values. |
| Method | SetNonUniformData | Obsolete. Superseded by ICWForce::Equation . |
| Method | SetReferenceGeometry | Sets the reference entity along whose direction this force is applied. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWForce::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for this time-dependent force in a dynamic study. |

[Top](#topBookmark)

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
