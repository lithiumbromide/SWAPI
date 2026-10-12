---
title: "AddFatigueEventForConstantAmplitude Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "AddFatigueEventForConstantAmplitude"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForConstantAmplitude.html"
---

# AddFatigueEventForConstantAmplitude Method (ICWFatigueStudyOptions)

Adds a fatigue event to a linear dynamic constant amplitude study.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFatigueEventForConstantAmplitude( _
   ByVal SAssociatedStudyName As System.String, _
   ByVal DScale As System.Double, _
   ByVal NStep As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWFatigueEvent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim SAssociatedStudyName As System.String
Dim DScale As System.Double
Dim NStep As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWFatigueEvent

value = instance.AddFatigueEventForConstantAmplitude(SAssociatedStudyName, DScale, NStep, ErrorCode)
```

### C#

```csharp
CWFatigueEvent AddFatigueEventForConstantAmplitude(
   System.string SAssociatedStudyName,
   System.double DScale,
   System.int NStep,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWFatigueEvent^ AddFatigueEventForConstantAmplitude(
   System.String^ SAssociatedStudyName,
   System.double DScale,
   System.int NStep,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SAssociatedStudyName`: Name of the reference study (see **Remarks**)
- `DScale`: 0.0 <= Factor by which to scale the result stresses of SAssociatedStudyName <= 1.0E36
- `NStep`: Solution step of SAssociatedStudyName; valid only for nonlinear or linear dynamic studies
- `ErrorCode`: Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

### Return Value

[ICWFatigueEvent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent.html)

## VBA Syntax

See [CWFatigueStudyOptions::AddFatigueEventForConstantAmplitude](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~AddFatigueEventForConstantAmplitude.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

SAssociatedStudyName must be the name of a study of the following type:

- Static
- Nonlinear

-or -

- Linear dynamic time History

To get or set the interaction option for this event, call [ICWFatigueStudyOptions::ConstantAmplitudeEventInteractionOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ConstantAmplitudeEventInteractionOption.html).

To fully configure the constant amplitude fatigue study for this event, call:

- [ICWFatigueStudyOptions::ComputingAlternatingStressOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ComputingAlternatingStressOption.html)
- [ICWFatigueStudyOptions::FatigueStrengthReductionFactor](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~FatigueStrengthReductionFactor.html)
- [ICWFatigueStudyOptions::MeanStressCorrectionOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~MeanStressCorrectionOption.html)
- [ICWFatigueStudyOptions::ResultFolder](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ResultFolder.html)
- [ICWFatigueStudyOptions::ShellFace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ShellFace.html)
- [ICWFatigueStudyOptions::SetInfiniteLifeSettings](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings.html)

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::AddFatigueEventForHarmonic Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForHarmonic.html)
[ICWFatigueStudyOptions::AddFatigueEventForRandomVibration Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForRandomVibration.html)
[ICWFatigueStudyOptions::AddFatigueEventForVariableAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html)
[ICWFatigueStudyOptions::DeleteFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~DeleteFatigueEvent.html)
[ICWFatigueStudyOptions::GetFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
