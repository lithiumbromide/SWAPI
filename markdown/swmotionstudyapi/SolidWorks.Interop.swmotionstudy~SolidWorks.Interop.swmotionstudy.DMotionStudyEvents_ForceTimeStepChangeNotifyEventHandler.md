---
title: "DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler.html"
---

# DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired when a motion study is [calculated](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~Calculate.html) and there are [external forces.](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationForceFeatureData~ExternalState.html)

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler( _
   ByVal Force As System.String, _
   ByVal Time As System.Double, _
   ByRef ForceMagnitude As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler(
   System.string Force,
   System.double Time,
   ref System.double ForceMagnitude
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler(
   System.String^ Force,
   System.double Time,
   System.double% ForceMagnitude
)
```

### Parameters

- `Force`: Force name
- `Time`: Time
- `ForceMagnitude`: New force or torque magnitude

## Visual Basic Application (VBA) Syntax

See [ForceTimeStepChangeNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~ForceTimeStepChangeNotify_EV.html).

## Remarks

If developing a C++ application, then use [swMotionStudyForceTimeStepChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

You can implement any force law after catching this event. The return value is a double that specifies the new force or torque magnitude. This event is called at every major time step from ADAMS.

## Availability

SOLIDWORKS 2008 SP01, Revision Number 16.1
