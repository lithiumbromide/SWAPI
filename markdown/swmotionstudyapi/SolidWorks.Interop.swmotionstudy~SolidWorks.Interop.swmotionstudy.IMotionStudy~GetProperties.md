---
title: "GetProperties Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetProperties"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetProperties.html"
---

# GetProperties Method (IMotionStudy)

Gets the properties object for the specified type of motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProperties( _
   ByVal StudyType As System.Integer _
) As MotionStudyProperties
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim StudyType As System.Integer
Dim value As MotionStudyProperties

value = instance.GetProperties(StudyType)
```

### C#

```csharp
MotionStudyProperties GetProperties(
   System.int StudyType
)
```

### C++/CLI

```cpp
MotionStudyProperties^ GetProperties(
   System.int StudyType
)
```

### Parameters

- `StudyType`: Type of motion study as defined by [swMotionStudyType_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyType_e.html)

### Return Value

[Properties object for the specified motion study](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyProperties.html)

## VBA Syntax

See [MotionStudy::GetProperties](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetProperties.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)
[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
