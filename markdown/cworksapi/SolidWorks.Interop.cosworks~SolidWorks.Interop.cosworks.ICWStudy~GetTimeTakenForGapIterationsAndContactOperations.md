---
title: "GetTimeTakenForGapIterationsAndContactOperations Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "GetTimeTakenForGapIterationsAndContactOperations"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForGapIterationsAndContactOperations.html"
---

# GetTimeTakenForGapIterationsAndContactOperations Method (ICWStudy)

Gets the time taken for gap iterations and contact operations in this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeTakenForGapIterationsAndContactOperations() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.GetTimeTakenForGapIterationsAndContactOperations()
```

### C#

```csharp
System.int GetTimeTakenForGapIterationsAndContactOperations()
```

### C++/CLI

```cpp
System.int GetTimeTakenForGapIterationsAndContactOperations();
```

### Return Value

Time taken in seconds for gap iterations and contact operations in this nonlinear study

## VBA Syntax

See [CWStudy::GetTimeTakenforGapIterationsAndContactOperations](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~GetTimeTakenforGapIterationsAndContactOperations.html).

## Remarks

This method is valid only for nonlinear studies.

`model_name`**-**`study_name`**.out** is created after the study is analyzed and contains this time taken for gap iterations and contact operations. Check the location of this file in the results folder that is configered in **Simulation > Options > Default Options**.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::GetTimeTakenForInputDataTransferFromDatabase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputDataTransferFromDatabase.html)
[ICWStudy::GetTimeTakenForInputPhase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputPhase.html)
[ICWStudy::GetTotalSolutionTime Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTotalSolutionTime.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
