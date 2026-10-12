---
title: "DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler.html"
---

# DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired at every integrator or output time step when a motion simulation is occurring and [external forces](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationForceFeatureData~ExternalState.html) exist.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler( _
   ByVal Time As System.Double, _
   ByVal ForceNames As System.Object, _
   ByVal Displacement As System.Object, _
   ByVal Velocity As System.Object, _
   ByVal Acceleration As System.Object, _
   ByVal ForceOrTorque As System.Object, _
   ByRef ForceTorqueValue As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler(
   System.double Time,
   System.object ForceNames,
   System.object Displacement,
   System.object Velocity,
   System.object Acceleration,
   System.object ForceOrTorque,
   ref System.object ForceTorqueValue
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler(
   System.double Time,
   System.Object^ ForceNames,
   System.Object^ Displacement,
   System.Object^ Velocity,
   System.Object^ Acceleration,
   System.Object^ ForceOrTorque,
   System.Object^% ForceTorqueValue
)
```

### Parameters

- `Time`: Output time when the event is fired
- `ForceNames`: Array of strings containing the names of the external forces
- `Displacement`: Array of doubles indicating the position of each external force; the order of these values corresponds to the order of the names in ForceNames
- `Velocity`: Array of doubles indicating the velocity of each external force; the order of these values corresponds to the order of the names in ForceNames
- `Acceleration`: Array of doubles indicating the acceleration of each external force; the order of these values corresponds to the order of the names in ForceNames
- `ForceOrTorque`: Array of doubles indicating if an external force is a linear force or a rotary force (torque); the order of these values corresponds to the order of the names in ForceNames
- `ForceTorqueValue`: Array of doubles indicating the value of the force (position, velocity, or acceleration) at the next output time step; these values are used internally for doing interpolation during the integrator time steps; the order of these values corresponds to the order of the names in ForceNames

## Visual Basic Application (VBA) Syntax

See [ForceOutputTimeStepChangeNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~ForceOutputTimeStepChangeNotify_EV.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

When the motion simulation is occurring, the solver takes two types of time steps:

- integrator
- output

Integrator time steps are taken during the solve; thus, it is not guaranteed that the solver will actually converge at that step. Output time steps are taken after the solver has converged. By default, the ForceOutputTimeStepChangeNotify event is fired at integrator time steps. If you want to fire this event at output time steps, then set [IMotionStudy::SetFireOutputTimeStepEvents](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~SetFireOutputTimeStepEvents.html) to true.

If developing a C++ application, then use [swMotionStudyForceOutputTimeStepChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
