---
title: "DMotionStudyEvents_SpecialMotionEventNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_SpecialMotionEventNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_SpecialMotionEventNotifyEventHandler.html"
---

# DMotionStudyEvents_SpecialMotionEventNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired for motion-related special events, such as contacts.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_SpecialMotionEventNotifyEventHandler( _
   ByVal Time As System.Double, _
   ByVal EventType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_SpecialMotionEventNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_SpecialMotionEventNotifyEventHandler(
   System.double Time,
   System.int EventType
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_SpecialMotionEventNotifyEventHandler(
   System.double Time,
   System.int EventType
)
```

### Parameters

- `Time`: Time
- `EventType`: Motion-related special event as defined in [swSpecialMotionEventType_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swSpecialMotionEventType_e.html)

## Visual Basic Application (VBA) Syntax

See [SpecialMotionEventNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~SpecialMotionEventNotify_EV.html).

## Remarks

If developing a C++ application, then use [swMotionStudySpecialEventNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
