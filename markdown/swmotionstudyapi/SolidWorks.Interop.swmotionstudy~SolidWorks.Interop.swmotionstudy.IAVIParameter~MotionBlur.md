---
title: "MotionBlur Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "MotionBlur"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~MotionBlur.html"
---

# MotionBlur Property (IAVIParameter)

Gets or sets whether to enable motion blur when [saving an animation](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SaveToAVI.html) rendered using a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Property MotionBlur As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Boolean

instance.MotionBlur = value

value = instance.MotionBlur
```

### C#

```csharp
System.bool MotionBlur {get; set;}
```

### C++/CLI

```cpp
property System.bool MotionBlur {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to enable motion blur when saving an animation rendered using a ray-trace rendering engine, false to not (see **Remarks**)

## VBA Syntax

See [AVIParameter::MotionBlur](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~MotionBlur.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

A ray-trace rendering engine must be active to enable motion blur when saving an animation rendered using the engine.

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)
[IAVIParameter::BlurLength Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~BlurLength.html)
[IAVIParameter::BlurOffset Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~BlurOffset.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
