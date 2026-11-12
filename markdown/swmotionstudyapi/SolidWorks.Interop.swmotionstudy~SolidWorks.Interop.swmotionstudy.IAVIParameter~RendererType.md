---
title: "RendererType Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "RendererType"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~RendererType.html"
---

# RendererType Property (IAVIParameter)

Gets or sets the renderer type to save the animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property RendererType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.RendererType = value

value = instance.RendererType
```

### C#

```csharp
System.int RendererType {get; set;}
```

### C++/CLI

```cpp
property System.int RendererType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Renderer type as defined by [swRendererType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRendererType_e.html)

## VBA Syntax

See [AVIParameter::RendererType](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~RendererType.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

If the renderer type is set to Custom, then you can change the [height](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenHeight.html) and [width](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenWidth.html) of the animation, [preserve the aspect ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~PreserveRatio.html) of the animation, and set the aspect ratio to either the [screen ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenRatio.html) or a [value](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
