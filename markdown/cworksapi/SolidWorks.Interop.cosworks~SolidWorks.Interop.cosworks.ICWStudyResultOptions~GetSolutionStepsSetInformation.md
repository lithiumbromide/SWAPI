---
title: "GetSolutionStepsSetInformation Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "GetSolutionStepsSetInformation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSolutionStepsSetInformation.html"
---

# GetSolutionStepsSetInformation Method (ICWStudyResultOptions)

Gets solution steps information for the specified set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSolutionStepsSetInformation( _
   ByVal NSetNumber As System.Integer, _
   ByRef NStartStep As System.Integer, _
   ByRef NEndStep As System.Integer, _
   ByRef NStepIncrement As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim NSetNumber As System.Integer
Dim NStartStep As System.Integer
Dim NEndStep As System.Integer
Dim NStepIncrement As System.Integer

instance.GetSolutionStepsSetInformation(NSetNumber, NStartStep, NEndStep, NStepIncrement)
```

### C#

```csharp
void GetSolutionStepsSetInformation(
   System.int NSetNumber,
   out System.int NStartStep,
   out System.int NEndStep,
   out System.int NStepIncrement
)
```

### C++/CLI

```cpp
void GetSolutionStepsSetInformation(
   System.int NSetNumber,
   [Out] System.int NStartStep,
   [Out] System.int NEndStep,
   [Out] System.int NStepIncrement
)
```

### Parameters

- `NSetNumber`: Solution steps set number (1-5)
- `NStartStep`: 1 <= Starting step <= 10000
- `NEndStep`: 1 <= Ending step <= 10000
- `NStepIncrement`: 1 <= Step increment <= 10000

## VBA Syntax

See [CWStudyResultOptions::GetSolutionStepsSetInformation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~GetSolutionStepsSetInformation.html).

## Remarks

This method is valid only if [ICWStudyResultOptions::SaveResultsForSolutionStepsOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html) = swsSaveResultsOption_e.swsSaveResultsOption_ForSpecifiedSolutionSteps.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::SetSolutionStepsSetInformation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSolutionStepsSetInformation.html)
[ICWStudyResultOptions::SaveResultsForSolutionStepsOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
