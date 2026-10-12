---
title: "GetTimeTakenForInputDataTransferFromDatabase Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "GetTimeTakenForInputDataTransferFromDatabase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputDataTransferFromDatabase.html"
---

# GetTimeTakenForInputDataTransferFromDatabase Method (ICWStudy)

Gets the time taken for input data transfer from the database in this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeTakenForInputDataTransferFromDatabase() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.GetTimeTakenForInputDataTransferFromDatabase()
```

### C#

```csharp
System.int GetTimeTakenForInputDataTransferFromDatabase()
```

### C++/CLI

```cpp
System.int GetTimeTakenForInputDataTransferFromDatabase();
```

### Return Value

Time taken in seconds for input data transfer from the database in this nonlinear study

## VBA Syntax

See [CWStudy::GetTimeTakenForInputDataTransferFromDatabase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~GetTimeTakenForInputDataTransferFromDatabase.html).

## Remarks

This method is valid only for nonlinear studies.

`model_name`**-**`study_name`**.out** is created after the study is analyzed and contains this time taken for input data transfer from the database. Check the location of this file in the results folder that is configered in **Simulation > Options > Default Options**.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::GetTimeTakenForGapIterationsAndContactOperations Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForGapIterationsAndContactOperations.html)
[ICWStudy::GetTimeTakenForInputPhase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTimeTakenForInputPhase.html)
[ICWStudy::GetTotalSolutionTime Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetTotalSolutionTime.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
