---
title: "SetArcLengthCompletionOptions Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SetArcLengthCompletionOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetArcLengthCompletionOptions.html"
---

# SetArcLengthCompletionOptions Method (ICWNonLinearStudyOptions)

Sets arc-length completion options for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetArcLengthCompletionOptions( _
   ByVal DMaxLoad As System.Double, _
   ByVal DMaxDisplacement As System.Double, _
   ByVal NUnit As System.Integer, _
   ByVal NArcSteps As System.Integer, _
   ByVal DArcLenMultiplier As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim DMaxLoad As System.Double
Dim DMaxDisplacement As System.Double
Dim NUnit As System.Integer
Dim NArcSteps As System.Integer
Dim DArcLenMultiplier As System.Double
Dim value As System.Integer

value = instance.SetArcLengthCompletionOptions(DMaxLoad, DMaxDisplacement, NUnit, NArcSteps, DArcLenMultiplier)
```

### C#

```csharp
System.int SetArcLengthCompletionOptions(
   System.double DMaxLoad,
   System.double DMaxDisplacement,
   System.int NUnit,
   System.int NArcSteps,
   System.double DArcLenMultiplier
)
```

### C++/CLI

```cpp
System.int SetArcLengthCompletionOptions(
   System.double DMaxLoad,
   System.double DMaxDisplacement,
   System.int NUnit,
   System.int NArcSteps,
   System.double DArcLenMultiplier
)
```

### Parameters

- `DMaxLoad`: Maximum load pattern multiplier
- `DMaxDisplacement`: Maximum displacement (for translational DOF)
- `NUnit`: Units as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)
- `NArcSteps`: Maximum number of arc steps
- `DArcLenMultiplier`: Initial arc length multiplier

### Return Value

Status as defined in [swsNonLinearStudyOptionsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonLinearStudyOptionsError_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::SetArcLengthCompletionOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SetArcLengthCompletionOptions.html).

## Remarks

[ICWNonLinearStudyOptions::ControlMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ControlMethodType.html) must be set to [swsNonLinearOptionControlMethodType_e.swsNonLinearControl_ArcLength](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonLinearOptionControlMethodType_e.html) to set arc-length completion options.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetArcLengthCompletionOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetArcLengthCompletionOptions.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0
