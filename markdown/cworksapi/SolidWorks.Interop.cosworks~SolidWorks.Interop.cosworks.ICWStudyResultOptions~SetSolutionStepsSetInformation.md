---
title: "SetSolutionStepsSetInformation Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SetSolutionStepsSetInformation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSolutionStepsSetInformation.html"
---

# SetSolutionStepsSetInformation Method (ICWStudyResultOptions)

Sets solution steps set information.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSolutionStepsSetInformation( _
   ByVal NSetNumber As System.Integer, _
   ByVal NStartStep As System.Integer, _
   ByVal NEndStep As System.Integer, _
   ByVal NStepIncrement As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim NSetNumber As System.Integer
Dim NStartStep As System.Integer
Dim NEndStep As System.Integer
Dim NStepIncrement As System.Integer
Dim value As System.Integer

value = instance.SetSolutionStepsSetInformation(NSetNumber, NStartStep, NEndStep, NStepIncrement)
```

### C#

```csharp
System.int SetSolutionStepsSetInformation(
   System.int NSetNumber,
   System.int NStartStep,
   System.int NEndStep,
   System.int NStepIncrement
)
```

### C++/CLI

```cpp
System.int SetSolutionStepsSetInformation(
   System.int NSetNumber,
   System.int NStartStep,
   System.int NEndStep,
   System.int NStepIncrement
)
```

### Parameters

- `NSetNumber`: Solution steps set number (1-5)
- `NStartStep`: 1 <= Starting step <= 10000
- `NEndStep`: 1 <= Ending step <= 10000
- `NStepIncrement`: 1 <= Step increment <= 10000

### Return Value

Status code as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWStudyResultOptions::SetSolutionStepsSetInformation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~SetSolutionStepsSetInformation.html).

## Examples

See the [ICWStudyResultOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html) examples.

## Remarks

This method is valid only if [ICWStudyResultOptions::SaveResultsForSolutionStepsOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html) = [swsSaveResultsOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSaveResultsOption_e.html).swsSaveResultsOption_ForSpecifiedSolutionSteps.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::GetSolutionStepsSetInformation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSolutionStepsSetInformation.html)
[ICWStudyResultOptions::SaveResultsForSolutionStepsOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
