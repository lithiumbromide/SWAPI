---
title: "ISimulationMotorFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html"
---

# ISimulationMotorFeatureData Interface Members

The following tables list the members exposed by [ISimulationMotorFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | DirectionReference | Gets or sets the direction in which the motor moves. |
| Property | DriveType | Sets the drive type of this motor feature. |
| Property | Expression | Gets or sets the motor motion expression for this motor feature. |
| Property | ExternalState | Gets or sets whether your application can listen to motor-related motion study event. |
| Property | InterpolationScheme | Gets or set the interpolation scheme for this motor feature. |
| Property | LoadReferences | Gets or sets the load references for this motor feature. |
| Property | Location | Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part. |
| Property | Magnitude | Get or set the magnitude for this motor feature. |
| Property | MotionType | Gets or sets the type of motion of this motor feature. |
| Property | MotorType | Gets the type of motor for this motor feature. |
| Property | RelativeComponent | Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature. |
| Property | ReverseDirection | Gets or sets whether or not to reverse the direction of the motor. |
| Property | SplineData | Gets or sets the spline data points for this motor feature. |
| Property | Velocity | Gets or sets the speed of the motor if no other force acts on it. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ConstantSpeedMotor | Sets the constant speed for this motor feature. |
| Method | DistanceMotor | Sets the distance and time for which to operate this motor feature. |
| Method | GetInterpolatedValue | Gets the interopolated value at the specified time for this motor feature. |
| Method | InterpolatedMotor | Sets the drive type and interpolation scheme for this motor feature. |
| Method | LoadSplineData | Loads the spline data from the specified file for this motor feature. |
| Method | OscillatingMotor | Sets the displacement and frequency for oscillating motion for this motor feature. |

[Top](#topBookmark)

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[Simulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[SimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[SimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
