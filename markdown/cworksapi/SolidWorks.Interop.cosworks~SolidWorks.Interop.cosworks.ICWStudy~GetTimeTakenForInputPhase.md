---
title: "GetTimeTakenForInputPhase Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "GetTimeTakenForInputPhase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputPhase.html"
---

# GetTimeTakenForInputPhase Method (ICWStudy)

Gets the time taken for the input phase of this static study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeTakenForInputPhase() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.GetTimeTakenForInputPhase()
```

### C#

```csharp
System.int GetTimeTakenForInputPhase()
```

### C++/CLI

```cpp
System.int GetTimeTakenForInputPhase();
```

### Return Value

Time taken in seconds for the input phase of this static study

## VBA Syntax

See [CWStudy::GetTimeTakenForInputPhase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~GetTimeTakenForInputPhase.html).

## Examples

[Create Plots for Static Study (VBA)](Create_Plots_for_Static_Study_Example_VB.htm)
[Create Plots for Static Study (VB.NET)](Create_Plots_for_Static_Study_Example_VBNET.htm)
[Create Plots for Static Study (C#)](Create_Plots_for_Static_Study_Example_CSharp.htm)

## Remarks

This method is valid only for static studies.

`model_name`**-**`study_name`**.out** is created after the study is analyzed and contains this time taken for the input phase. Check the location of this file in the results folder that is configered in **Simulation > Options > Default Options**.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::GetTimeTakenForGapIterationsAndContactOperations Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForGapIterationsAndContactOperations.html)
[ICWStudy::GetTimeTakenForInputDataTransferFromDatabase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputDataTransferFromDatabase.html)
[ICWStudy::GetTotalSolutionTime Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTotalSolutionTime.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
