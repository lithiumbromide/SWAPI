---
title: "DMotionStudyEvents_PartCollideNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "DMotionStudyEvents_PartCollideNotifyEventHandler"
member: ""
kind: "topic"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.DMotionStudyEvents_PartCollideNotifyEventHandler.html"
---

# DMotionStudyEvents_PartCollideNotifyEventHandler Delegate (SolidWorks.Interop.swmotionstudy)

Fired when a collision between two components occurs.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMotionStudyEvents_PartCollideNotifyEventHandler( _
   ByVal Time As System.Double, _
   ByVal Component1 As System.Object, _
   ByVal Component2 As System.Object, _
   ByVal Vector1 As System.Object, _
   ByVal Vector2 As System.Object, _
   ByVal SurfaceNormal1 As System.Object, _
   ByVal SurfaceNormal2 As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMotionStudyEvents_PartCollideNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMotionStudyEvents_PartCollideNotifyEventHandler(
   System.double Time,
   System.object Component1,
   System.object Component2,
   System.object Vector1,
   System.object Vector2,
   System.object SurfaceNormal1,
   System.object SurfaceNormal2
)
```

### C++/CLI

```cpp
public delegate System.int DMotionStudyEvents_PartCollideNotifyEventHandler(
   System.double Time,
   System.Object^ Component1,
   System.Object^ Component2,
   System.Object^ Vector1,
   System.Object^ Vector2,
   System.Object^ SurfaceNormal1,
   System.Object^ SurfaceNormal2
)
```

### Parameters

- `Time`: Time of collision
- `Component1`: [Component 1](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
- `Component2`: [Component 2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
- `Vector1`: [Point](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) on Component1
- `Vector2`: [Point](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) on Component 2
- `SurfaceNormal1`: Surface normal of Component 1
- `SurfaceNormal2`: Surface normal of Component 2

## Visual Basic Application (VBA) Syntax

See [PartCollideNotify Event (MotionStudy)](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~PartCollideNotify_EV.html).

## Remarks

If developing a C++ application, then use [swMotionStudyPartCollideNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 SP01, Revision Number 16.1
