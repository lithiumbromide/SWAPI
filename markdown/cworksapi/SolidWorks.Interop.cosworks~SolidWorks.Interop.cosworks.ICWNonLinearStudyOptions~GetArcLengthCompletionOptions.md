---
title: "GetArcLengthCompletionOptions Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetArcLengthCompletionOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetArcLengthCompletionOptions.html"
---

# GetArcLengthCompletionOptions Method (ICWNonLinearStudyOptions)

Gets the arc-length completion options for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetArcLengthCompletionOptions( _
   ByRef DMaxLoad As System.Double, _
   ByRef DMaxDisplacement As System.Double, _
   ByRef NUnit As System.Integer, _
   ByRef NMaxArcSteps As System.Integer, _
   ByRef DArcLengthMultiplier As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim DMaxLoad As System.Double
Dim DMaxDisplacement As System.Double
Dim NUnit As System.Integer
Dim NMaxArcSteps As System.Integer
Dim DArcLengthMultiplier As System.Double

instance.GetArcLengthCompletionOptions(DMaxLoad, DMaxDisplacement, NUnit, NMaxArcSteps, DArcLengthMultiplier)
```

### C#

```csharp
void GetArcLengthCompletionOptions(
   out System.double DMaxLoad,
   out System.double DMaxDisplacement,
   out System.int NUnit,
   out System.int NMaxArcSteps,
   out System.double DArcLengthMultiplier
)
```

### C++/CLI

```cpp
void GetArcLengthCompletionOptions(
   [Out] System.double DMaxLoad,
   [Out] System.double DMaxDisplacement,
   [Out] System.int NUnit,
   [Out] System.int NMaxArcSteps,
   [Out] System.double DArcLengthMultiplier
)
```

### Parameters

- `DMaxLoad`: Maximum load-pattern multiplier
- `DMaxDisplacement`: Maximum displacement (for translational DOF)
- `NUnit`: Units as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)
- `NMaxArcSteps`: Maximum number of arc steps
- `DArcLengthMultiplier`: Initial arc length multiplier

## VBA Syntax

See [CWNonLinearStudyOptions::GetArcLengthCompletionOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetArcLengthCompletionOptions.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinaerStudyOptions::SetArcLengthCompletionOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetArcLengthCompletionOptions.html)
[ICWNonLinaerStudyOptions::ControlMethodType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ControlMethodType.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0
