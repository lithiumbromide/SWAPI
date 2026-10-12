---
title: "GetResults Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetResults"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetResults.html"
---

# GetResults Method (IMotionStudy)

Gets the results object for the specified type of motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResults( _
   ByVal StudyType As System.Integer _
) As MotionStudyResults
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim StudyType As System.Integer
Dim value As MotionStudyResults

value = instance.GetResults(StudyType)
```

### C#

```csharp
MotionStudyResults GetResults(
   System.int StudyType
)
```

### C++/CLI

```cpp
MotionStudyResults^ GetResults(
   System.int StudyType
)
```

### Parameters

- `StudyType`: Type of motion study as defined by [swMotionStudyType_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyType_e.html)

### Return Value

[Results object for the specified type of motion study](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyResults.html)

## VBA Syntax

See [MotionStudy::GetResults](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetResults.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
