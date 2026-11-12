---
title: "SaveToAVI Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "SaveToAVI"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SaveToAVI.html"
---

# SaveToAVI Method (IMotionStudy)

Saves the animation to a .avi, .bmp, or .tga file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveToAVI( _
   ByVal FileName As System.String, _
   ByVal Parameter As AVIParameter _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim FileName As System.String
Dim Parameter As AVIParameter
Dim value As System.Boolean

value = instance.SaveToAVI(FileName, Parameter)
```

### C#

```csharp
System.bool SaveToAVI(
   System.string FileName,
   AVIParameter Parameter
)
```

### C++/CLI

```cpp
System.bool SaveToAVI(
   System.String^ FileName,
   AVIParameter^ Parameter
)
```

### Parameters

- `FileName`: Path and filename where to save a .avi, .bmp, or .tga file
- `Parameter`: [Parameters](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter.html) for the .avi file

### Return Value

True if the animation is saved to the specified file, false if not

## VBA Syntax

See [MotionStudy::SaveToAVI](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~SaveToAVI.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IAVIParameter::MotionBlur Property ()](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~MotionBlur.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
