---
title: "FramePerSecond Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "FramePerSecond"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~FramePerSecond.html"
---

# FramePerSecond Property (IAVIParameter)

Gets or sets the frames per second in which to play the animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property FramePerSecond As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Double

instance.FramePerSecond = value

value = instance.FramePerSecond
```

### C#

```csharp
System.double FramePerSecond {get; set;}
```

### C++/CLI

```cpp
property System.double FramePerSecond {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Frames per second in which to play the animation

## VBA Syntax

See [AVIParameter::FramePerSecond](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~FramePerSecond.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
