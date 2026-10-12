---
title: "AddFatigueEventForVariableAmplitude Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "AddFatigueEventForVariableAmplitude"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html"
---

# AddFatigueEventForVariableAmplitude Method (ICWFatigueStudyOptions)

Adds a fatigue event to a linear dynamic variable amplitude study.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFatigueEventForVariableAmplitude( _
   ByVal SAssociatedStudyName As System.String, _
   ByVal DScale As System.Double, _
   ByVal NStep As System.Integer, _
   ByVal VarLHCurveXData As System.Object, _
   ByVal VarLHCurveYData As System.Object, _
   ByVal NLHCurveType As System.Integer, _
   ByVal DSamplingRate As System.Double, _
   ByRef ErrorCode As System.Integer _
) As CWFatigueEvent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim SAssociatedStudyName As System.String
Dim DScale As System.Double
Dim NStep As System.Integer
Dim VarLHCurveXData As System.Object
Dim VarLHCurveYData As System.Object
Dim NLHCurveType As System.Integer
Dim DSamplingRate As System.Double
Dim ErrorCode As System.Integer
Dim value As CWFatigueEvent

value = instance.AddFatigueEventForVariableAmplitude(SAssociatedStudyName, DScale, NStep, VarLHCurveXData, VarLHCurveYData, NLHCurveType, DSamplingRate, ErrorCode)
```

### C#

```csharp
CWFatigueEvent AddFatigueEventForVariableAmplitude(
   System.string SAssociatedStudyName,
   System.double DScale,
   System.int NStep,
   System.object VarLHCurveXData,
   System.object VarLHCurveYData,
   System.int NLHCurveType,
   System.double DSamplingRate,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWFatigueEvent^ AddFatigueEventForVariableAmplitude(
   System.String^ SAssociatedStudyName,
   System.double DScale,
   System.int NStep,
   System.Object^ VarLHCurveXData,
   System.Object^ VarLHCurveYData,
   System.int NLHCurveType,
   System.double DSamplingRate,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SAssociatedStudyName`: Name of the reference study (see **Remarks**)
- `DScale`: 0.0 <= Factor by which to scale the result stresses of SAssociatedStudyName to produce fatigue <= 1.0E36
- `NStep`: Solution step of SAssociatedStudyName; valid only for nonlinear or linear dynamic - time history studies
- `VarLHCurveXData`: Array of times; valid only if NType = [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html).swsFatigueLoadHistoryCurveType_TimeAndAmplitude
- `VarLHCurveYData`: Array of amplitudes
- `NLHCurveType`: Type of curve as defined in [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html)
- `DSamplingRate`: Sampling rate in seconds; valid only if NType = [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html).swsFatigueLoadHistoryCurveType_SamplingRateAndAmplitude
- `ErrorCode`: Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

### Return Value

[ICWFatigueEvent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent.html)

## VBA Syntax

See [CWFatigueStudyOptions::AddFatigueEventForVariableAmplitude](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

SAssociatedStudyName must be the name of a study of the following type:

- Static
- Nonlinear

-or -

- Linear dynamic time History

To set the options for this event, call [ICWFatigueStudyOptions::SetVariableAmplitudeEventOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetVariableAmplitudeEventOptions.html).

To fully configure the variable amplitude fatigue study for this event, call:

- [ICWFatigueStudyOptions::ComputingAlternatingStressOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ComputingAlternatingStressOption.html)
- [ICWFatigueStudyOptions::FatigueStrengthReductionFactor](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~FatigueStrengthReductionFactor.html)
- [ICWFatigueStudyOptions::MeanStressCorrectionOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~MeanStressCorrectionOption.html)
- [ICWFatigueStudyOptions::ResultFolder](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ResultFolder.html)
- [ICWFatigueStudyOptions::ShellFace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ShellFace.html)
- [ICWFatigueStudyOptions::SetInfiniteLifeSettings](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings.html)

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::AddFatigueEventForConstantAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForConstantAmplitude.html)
[ICWFatigueStudyOptions::AddFatigueEventForHarmonic Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForHarmonic.html)
[ICWFatigueStudyOptions::AddFatigueEventForRandomVibration Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForRandomVibration.html)
[ICWFatigueStudyOptions::DeleteFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~DeleteFatigueEvent.html)
[ICWFatigueStudyOptions::GetFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
