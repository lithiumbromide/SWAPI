---
title: "AddFatigueEventForHarmonic Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "AddFatigueEventForHarmonic"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForHarmonic.html"
---

# AddFatigueEventForHarmonic Method (ICWFatigueStudyOptions)

Adds a fatigue event to a linear dynamic harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFatigueEventForHarmonic( _
   ByVal SAssociatedStudyName As System.String, _
   ByVal DFrequency As System.Double, _
   ByVal NPlotStep As System.Integer, _
   ByVal DCycles As System.Double, _
   ByVal DScale As System.Double, _
   ByRef ErrorCode As System.Integer _
) As CWFatigueEvent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim SAssociatedStudyName As System.String
Dim DFrequency As System.Double
Dim NPlotStep As System.Integer
Dim DCycles As System.Double
Dim DScale As System.Double
Dim ErrorCode As System.Integer
Dim value As CWFatigueEvent

value = instance.AddFatigueEventForHarmonic(SAssociatedStudyName, DFrequency, NPlotStep, DCycles, DScale, ErrorCode)
```

### C#

```csharp
CWFatigueEvent AddFatigueEventForHarmonic(
   System.string SAssociatedStudyName,
   System.double DFrequency,
   System.int NPlotStep,
   System.double DCycles,
   System.double DScale,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWFatigueEvent^ AddFatigueEventForHarmonic(
   System.String^ SAssociatedStudyName,
   System.double DFrequency,
   System.int NPlotStep,
   System.double DCycles,
   System.double DScale,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SAssociatedStudyName`: Name of the reference linear dynamic harmonic study (see **Remarks**)
- `DFrequency`: Frequency of SAssociatedStudyName; valid only if NPlotStep is 0
- `NPlotStep`: Solution step number of SAssociatedStudyName; valid only if DFrequency is 0
- `DCycles`: 1.0 < Number of cycles associated with this event < 1.0E36
- `DScale`: 0.0 <= Factor by which to scale the result stresses of SAssociatedStudyName to produce fatigue <= 1.0E36
- `ErrorCode`: Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

### Return Value

[ICWFatigueEvent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent.html)

## VBA Syntax

See [CWFatigueStudyOptions::AddFatigueEventForHarmonic](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~AddFatigueEventForHarmonic.html).

## Examples

[Create Fatigue Study for Dynamic Harmonic Study (VBA)](Create_Fatigue_Study_for_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Harmonic Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Harmonic Study (C#)](Create_Fatigue_Study_for_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

This method works only in SOLIDWORKS Simulation Premium.

Before running a fatigue harmonic study, apply material with defined fatigue S-N curves to the model parts of SAssociatedStudyName.

To fully configure the harmonic fatigue study for this event, call:

- [ICWFatigueStudyOptions::FatigueStrengthReductionFactor](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~FatigueStrengthReductionFactor.html)
- [ICWFatigueStudyOptions::ResultFolder](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ResultFolder.html)
- [ICWFatigueStudyOptions::ShellFace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ShellFace.html)
- [ICWFatigueStudyOptions::SetInfiniteLifeSettings](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings.html)

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::AddFatigueEventForConstantAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForConstantAmplitude.html)
[ICWFatigueStudyOptions::AddFatigueEventForRandomVibration Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForRandomVibration.html)
[ICWFatigueStudyOptions::AddFatigueEventForVariableAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html)
[ICWFatigueStudyOptions::DeleteFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~DeleteFatigueEvent.html)
[ICWFatigueStudyOptions::GetFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
