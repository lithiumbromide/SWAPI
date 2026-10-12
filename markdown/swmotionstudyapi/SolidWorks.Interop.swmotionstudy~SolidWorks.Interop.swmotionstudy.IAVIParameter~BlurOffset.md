---
title: "BlurOffset Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "BlurOffset"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~BlurOffset.html"
---

# BlurOffset Property (IAVIParameter)

Gets or sets the position in time from where the ray-trace rendering engine samples its motion blur for the animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlurOffset As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.BlurOffset = value

value = instance.BlurOffset
```

### C#

```csharp
System.int BlurOffset {get; set;}
```

### C++/CLI

```cpp
property System.int BlurOffset {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

| Value | Effect |
| --- | --- |
| 0 | Centers the motion blur on the current rendered frame |
| 100 | Moves the position forward one entire frame |
| -100 | Moves the position back one entire frame |

## VBA Syntax

See [AVIParameter::BlurOffset](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~BlurOffset.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)
[IAVIParameter::BlurLength Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~BlurLength.html)
[IAVIParameter::MotionBlur Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~MotionBlur.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
