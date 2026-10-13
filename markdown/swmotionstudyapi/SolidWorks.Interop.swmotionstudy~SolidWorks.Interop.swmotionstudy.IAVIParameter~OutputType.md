---
title: "OutputType Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "OutputType"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~OutputType.html"
---

# OutputType Property (IAVIParameter)

Gets or sets the type of files to which to save the animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property OutputType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.OutputType = value

value = instance.OutputType
```

### C#

```csharp
System.int OutputType {get; set;}
```

### C++/CLI

```cpp
property System.int OutputType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

File type as defined by [swAnimationOutputType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimationOutputType_e.html)

## VBA Syntax

See [AVIParameter::OutputType](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~OutputType.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
