---
title: "DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler.html"
---

# DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired when a motion study is [calculated](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~Calculate.html) and there are [external motors](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationMotorFeatureData~ExternalState.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler( _
   ByVal Motor As System.String, _
   ByVal Time As System.Double, _
   ByRef MotorSpeed As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler(
   System.string Motor,
   System.double Time,
   ref System.double MotorSpeed
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler(
   System.String^ Motor,
   System.double Time,
   System.double% MotorSpeed
)
```

### Parameters

- `Motor`: Motor name
- `Time`: Time
- `MotorSpeed`: New motor speed

## Visual Basic Application (VBA) Syntax

See [MotorTimeStepChangeNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~MotorTimeStepChangeNotify_EV.html).

## Remarks

If developing a C++ application, then use [swMotionStudyMotorTimeStepChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

You can implement any motion law after catching this event. The return value is a double that specifies the new motor speed. This event is called at every major time step from ADAMS.

## Availability

SOLIDWORKS 2008 SP01, Revision Number 16.1
