---
title: "DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler.html"
---

# DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired at every integrator or output time step when a motion simulation is occurring.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler( _
   ByVal Time As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler(
   System.double Time
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler(
   System.double Time
)
```

### Parameters

- `Time`: Output time when the event is fired

## Visual Basic Application (VBA) Syntax

See [OutputTimeStepChangeNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~OutputTimeStepChangeNotify_EV.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

When the motion simulation is occurring, the solver takes two types of time steps:

- integrator
- output

Integrator time steps are taken during the solve; thus, it is not guaranteed that the solver will actually converge at that step. Output time steps are taken after the solver has converged. By default, the OutputTimeStepChangeNotify event is fired at integrator time steps. If you want to fire this event at output time steps, then set [IMotionStudy::SetFireOutputTimeStepEvents](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~SetFireOutputTimeStepEvents.html) to true.

If developing a C++ application, then use [swMotionStudyOutputTimeStepChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
