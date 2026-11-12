---
title: "DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler.html"
---

# DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired at every integrator or output time step when a motion simulation is occurring and [external motors](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationMotorFeatureData~ExternalState.html) exist.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler( _
   ByVal Time As System.Double, _
   ByVal MotorNames As System.Object, _
   ByVal Position As System.Object, _
   ByVal Velocity As System.Object, _
   ByVal Acceleration As System.Object, _
   ByVal ForceOrTorque As System.Object, _
   ByRef MotorValue As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler(
   System.double Time,
   System.object MotorNames,
   System.object Position,
   System.object Velocity,
   System.object Acceleration,
   System.object ForceOrTorque,
   ref System.object MotorValue
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler(
   System.double Time,
   System.Object^ MotorNames,
   System.Object^ Position,
   System.Object^ Velocity,
   System.Object^ Acceleration,
   System.Object^ ForceOrTorque,
   System.Object^% MotorValue
)
```

### Parameters

- `Time`: Output time when the event is fired
- `MotorNames`: Array of strings containing the names of the external motors
- `Position`: Array of doubles indicating the position of each external motor; the order of these valeus corresponds to the order of the names of MotorNames
- `Velocity`: Array of doubles indicating the velocity of each external motor; the order of these values corresponds to the order of the names in MotorNames
- `Acceleration`: Array of doubles indicating the acceleration of each external motor; the order of these values corresponds to the order of the names in MotorNames
- `ForceOrTorque`: Array of doubles indicating if an external motor is a linear motor (force) or a rotary motor (torque); the order of these values corresponds to the order of the names in MotorNames
- `MotorValue`: Array of doubles indicating the value of the motor (position, velocity, or acceleration) at the next output time step; these values are used internally for doing interpolation during the integrator time steps; the order of these values corresponds to the order of the names in MotorNames

## Visual Basic Application (VBA) Syntax

See [MotorOutputTimeStepChangeNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~MotorOutputTimeStepChangeNotify_EV.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

When the motion simulation is occurring, the solver takes two types of time steps:

- integrator
- output

Integrator time steps are taken during the solve; thus, it is not guaranteed that the solver will actually converge at that step. Output time steps are taken after the solver has converged. By default, the MotorOutputTimeStepChangeNotify event is fired at integrator time steps. If you want to fire this event at output time steps, then set [IMotionStudy::SetFireOutputTimeStepEvents](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~SetFireOutputTimeStepEvents.html) to true.

If developing a C++ application, then use [swMotionStudyMotorOutputTimeStepChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
