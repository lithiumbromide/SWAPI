---
title: "GetSupportedStudyTypes Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetSupportedStudyTypes"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetSupportedStudyTypes.html"
---

# GetSupportedStudyTypes Method (IMotionStudy)

Gets the types of studies supported by this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSupportedStudyTypes( _
   ByRef SupportedTypes As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim SupportedTypes As System.Integer
Dim value As System.Boolean

value = instance.GetSupportedStudyTypes(SupportedTypes)
```

### C#

```csharp
System.bool GetSupportedStudyTypes(
   out System.int SupportedTypes
)
```

### C++/CLI

```cpp
System.bool GetSupportedStudyTypes(
   [Out] System.int SupportedTypes
)
```

### Parameters

- `SupportedTypes`: Type of motion study as defined by [swMotionStudyType_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyType_e.html)

### Return Value

True if this method runs successfully, false if not

## VBA Syntax

See [MotionStudy::GetSupportedStudyTypes](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetSupportedStudyTypes.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::StudyType Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~StudyType.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
