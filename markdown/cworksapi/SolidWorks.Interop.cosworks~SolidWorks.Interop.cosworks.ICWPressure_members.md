---
title: "ICWPressure Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html"
---

# ICWPressure Interface Members

The following tables list the members exposed by [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CoordSystemType | Gets or sets the type of coordinate system used to define this nonuniform pressure. |
| Property | DirectionType | Gets or sets how this pressure is applied along the specified reference geometry. |
| Property | Equation | Gets or sets the equation describing this pressure of nonuniform distribution. |
| Property | EquationAngularUnit | Gets or sets the angular units for cylindrical and spherical coordinate systems of the nonuniform pressure distribution equation. |
| Property | EquationLinearUnit | Gets or sets the linear units for Cartesian, cylindrical, and spherical coordinate systems of the nonuniform pressure distribution equation. |
| Property | IncludeNonUniformDistribution | Obsolete. Superseded by ICWPressure::IncludeNonUniformDistribution2 . |
| Property | IncludeNonUniformDistribution2 | Gets or sets whether to use a nonuniform distribution of pressure. |
| Property | PhaseAngle | Gets or sets the phase angle of the pressure in a linear dynamic harmonic study. |
| Property | PhaseAngleUnit | Gets or sets the units of phase angle of the pressure in a linear dynamic harmonic study. |
| Property | PressureType | Gets or sets the pressure direction type (normal or use reference geometry). |
| Property | ReverseDirection | Obsolete. Superseded by ICWPressure::ReverseDirection2 . |
| Property | ReverseDirection2 | Gets or sets whether to reverse the direction of this pressure. |
| Property | Unit | Gets or sets the units of pressure. |
| Property | Value | Gets or sets the pressure value. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetCoordinateSystem | Gets the coordinate system that defines this nonuniform pressure. |
| Method | GetNonUniformData | Obsolete. Superseded by ICWPressure::Equation . |
| Method | GetTimeCurve | Gets the time curve data for this time-dependent pressure in a dynamic study. |
| Method | InsertEntity | Inserts a face to which to apply this pressure. |
| Method | PressureBeginEdit | Starts editing pressure. |
| Method | PressureEndEdit | Ends editing pressure. |
| Method | RemoveEntity | Removes the entity at the specified index. |
| Method | SetCoordinateSystem | Sets the coordinate system that defines this nonuniform pressure. |
| Method | SetNonUniformData | Obsolete. Superseded by ICWPressure::Equation . |
| Method | SetReferenceGeometry | Sets the face, edge, plane, or axis to be used to set the direction of this pressure. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWPressure::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for this time-dependent pressure in a dynamic study. |

[Top](#topBookmark)

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
