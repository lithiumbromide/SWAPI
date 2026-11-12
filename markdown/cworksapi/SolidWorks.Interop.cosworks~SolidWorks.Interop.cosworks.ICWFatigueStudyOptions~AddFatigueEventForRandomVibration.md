---
title: "AddFatigueEventForRandomVibration Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "AddFatigueEventForRandomVibration"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForRandomVibration.html"
---

# AddFatigueEventForRandomVibration Method (ICWFatigueStudyOptions)

Adds a fatigue event to a linear dynamic random vibration study.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFatigueEventForRandomVibration( _
   ByVal SAssociatedStudyName As System.String, _
   ByVal DDuration As System.Double, _
   ByVal NUnitTime As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWFatigueEvent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim SAssociatedStudyName As System.String
Dim DDuration As System.Double
Dim NUnitTime As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWFatigueEvent

value = instance.AddFatigueEventForRandomVibration(SAssociatedStudyName, DDuration, NUnitTime, ErrorCode)
```

### C#

```csharp
CWFatigueEvent AddFatigueEventForRandomVibration(
   System.string SAssociatedStudyName,
   System.double DDuration,
   System.int NUnitTime,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWFatigueEvent^ AddFatigueEventForRandomVibration(
   System.String^ SAssociatedStudyName,
   System.double DDuration,
   System.int NUnitTime,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SAssociatedStudyName`: Name of the reference linear dynamic random vibration study
- `DDuration`: 0.0 <= Duration of the random loading input for this fatigue event <= 1.0E36
- `NUnitTime`: Units of time for DDuration as defined in [swsTimeUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTimeUnits_e.html)
- `ErrorCode`: Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

### Return Value

[ICWFatigueEvent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent.html)

## VBA Syntax

See [CWFatigueStudyOptions::AddFatigueEventForRandomVibration](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~AddFatigueEventForRandomVibration.html).

## Examples

[Create Fatigue Study for Dynamic Random Vibration Study (VBA)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (C#)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## Remarks

This method works only in SOLIDWORKS Simulation Premium.

To fully configure the random vibration fatigue study for this event, call:

- [ICWFatigueStudyOptions::RandomVibrationComputationalMethod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~RandomVibrationComputationalMethod.html)
- [ICWFatigueStudyOptions::FatigueStrengthReductionFactor](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~FatigueStrengthReductionFactor.html)
- [ICWFatigueStudyOptions::ResultFolder](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ResultFolder.html)
- [ICWFatigueStudyOptions::ShellFace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ShellFace.html)
- [ICWFatigueStudyOptions::SetInfiniteLifeSettings](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings.html)

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::AddFatigueEventForConstantAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForConstantAmplitude.html)
[ICWFatigueStudyOptions::AddFatigueEventForHarmonic Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForHarmonic.html)
[ICWFatigueStudyOptions::AddFatigueEventForVariableAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html)
[ICWFatigueStudyOptions::DeleteFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~DeleteFatigueEvent.html)
[ICWFatigueStudyOptions::GetFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
