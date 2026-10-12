---
title: "DMotionStudyEvents_StopCalculateNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_StopCalculateNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_StopCalculateNotifyEventHandler.html"
---

# DMotionStudyEvents_StopCalculateNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired when a motion study's calculation ends.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_StopCalculateNotifyEventHandler( _
   ByVal Time As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_StopCalculateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_StopCalculateNotifyEventHandler(
   System.double Time
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_StopCalculateNotifyEventHandler(
   System.double Time
)
```

### Parameters

- `Time`: Time when event fired (i.e., time at which calculations stop)

## Visual Basic Application (VBA) Syntax

See [StopCalculateNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~StopCalculateNotify_EV.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

If developing a C++ application, then use [swMotionStudyStopCalculateNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
