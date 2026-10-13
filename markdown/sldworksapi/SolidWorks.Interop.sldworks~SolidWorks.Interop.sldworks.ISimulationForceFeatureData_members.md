---
title: "ISimulationForceFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html"
---

# ISimulationForceFeatureData Interface Members

The following tables list the members exposed by [ISimulationForceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ActionDirection | Gets or sets the direction of the force. |
| Property | ActionLocation | Gets or sets the location at which to apply the force for an action-only force. |
| Property | ActionType | Gets or sets the type of action for this Force feature. |
| Property | ExternalState | Gets or sets whether your application can listen to force-related motion study events. |
| Property | ForceFunctionType | Gets or sets the type of function for this Force feature. |
| Property | ForceType | Gets the type of force. NOTE: This property is a get-only property. Set is not implemented. |
| Property | FunctionConstantValue | Gets or sets the function constant value for this Force feature. |
| Property | FunctionExpression | Gets or sets the expression function for this Force feature. |
| Property | FunctionInterpolatedValues | Gets or sets the interpolated values for this Force feature. |
| Property | InterpolationScheme | Gets the interopolation scheme for this Force feature. |
| Property | LoadReferences | Gets or sets the load references for this Force feature. |
| Property | ReactionLocation | Gets or sets the location at which to apply the force for an action/reaction force. |
| Property | ReferenceComponent | Gets or sets the component to serve as a reference frame for the force. |
| Property | ReverseDirection | Gets or sets whether to reverse the direction of the force. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetEndPoints | Gets the end points of this Force feature. |
| Method | GetFunctionHarmonicValues | Gets the harmonic function values for this Force feature. |
| Method | GetFunctionStepValues | Gets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature. |
| Method | GetInterpolatedValue | Gets the interpolated value at the specified time for this Force feature. |
| Method | LoadSplineData | Loads the spline data from the specified file for this Force feature. |
| Method | SetEndPoints | Sets the end points for this Force feature. |
| Method | SetFunctionHarmonicValues | Sets the harmonic function values for this Force feature. |
| Method | SetFunctionStepValues | Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature. |

[Top](#topBookmark)

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[Simulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[SimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
