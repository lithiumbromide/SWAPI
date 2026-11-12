---
title: "BlurLength Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "BlurLength"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~BlurLength.html"
---

# BlurLength Property (IAVIParameter)

Gets or sets the length of the motion blur effect when rendering animations using a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlurLength As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.BlurLength = value

value = instance.BlurLength
```

### C#

```csharp
System.int BlurLength {get; set;}
```

### C++/CLI

```cpp
property System.int BlurLength {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 <= Length of the motion blur effect when rendering animations using a ray-trace rendering engine <= 100; default = 50

## VBA Syntax

See [AVIParameter::BlurLength](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~BlurLength.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study(VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)
[IAVIParameter::BlurOffset Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~BlurOffset.html)
[IAVIParameter::MotionBlur Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~MotionBlur.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
