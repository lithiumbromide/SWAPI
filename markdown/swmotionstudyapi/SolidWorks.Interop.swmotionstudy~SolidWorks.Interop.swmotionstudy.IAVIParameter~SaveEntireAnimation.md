---
title: "SaveEntireAnimation Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "SaveEntireAnimation"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~SaveEntireAnimation.html"
---

# SaveEntireAnimation Property (IAVIParameter)

Gets or sets whether to save the entire animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveEntireAnimation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Boolean

instance.SaveEntireAnimation = value

value = instance.SaveEntireAnimation
```

### C#

```csharp
System.bool SaveEntireAnimation {get; set;}
```

### C++/CLI

```cpp
property System.bool SaveEntireAnimation {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to save the entire animation, false to not

## VBA Syntax

See [AVIParameter::SaveEntireAnimation](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~SaveEntireAnimation.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

If this property is set to false, then specify the [start time](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~StartTime.html) and [end time](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~EndTime.html) of the time period of the animation to which to save to the animation file or files.

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)
[IAVIParameter::ScreenHeight Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ScreenHeight.html)
[IAVIParameter::ScreenWidth Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ScreenWidth.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
