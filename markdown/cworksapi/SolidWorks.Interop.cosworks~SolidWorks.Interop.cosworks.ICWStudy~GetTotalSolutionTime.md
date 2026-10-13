---
title: "GetTotalSolutionTime Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "GetTotalSolutionTime"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTotalSolutionTime.html"
---

# GetTotalSolutionTime Method (ICWStudy)

Gets the total solver time for this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalSolutionTime() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.GetTotalSolutionTime()
```

### C#

```csharp
System.int GetTotalSolutionTime()
```

### C++/CLI

```cpp
System.int GetTotalSolutionTime();
```

### Return Value

Total solver time in seconds for this study

## VBA Syntax

See [CWStudy::GetTotalSolutionTime](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~GetTotalSolutionTime.html).

## Examples

[Create Plots for Static Study (VBA)](Create_Plots_for_Static_Study_Example_VB.htm)
[Create Plots for Static Study (VB.NET)](Create_Plots_for_Static_Study_Example_VBNET.htm)
[Create Plots for Static Study (C#)](Create_Plots_for_Static_Study_Example_CSharp.htm)

## Remarks

This method is valid for both static and nonlinear studies.

`model_name`**-**`study_name`**.out** is created after the study is analyzed and contains this total solver time. Check the location of this file in the results folder that is configered in **Simulation > Options > Default Options**.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::GetTimeTakenForGapIterationsAndContactOperations Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForGapIterationsAndContactOperations.html)
[ICWStudy::GetTimeTakenForInputDataTransferFromDatabase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputDataTransferFromDatabase.html)
[ICWStudy::GetTimeTakenForInputPhase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputPhase.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
