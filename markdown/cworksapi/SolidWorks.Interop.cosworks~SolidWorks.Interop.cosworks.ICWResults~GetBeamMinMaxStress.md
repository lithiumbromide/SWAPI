---
title: "GetBeamMinMaxStress Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetBeamMinMaxStress"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamMinMaxStress.html"
---

# GetBeamMinMaxStress Method (ICWResults)

Gets the minimum and maximum elemental stresses for beams at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBeamMinMaxStress( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetBeamMinMaxStress(NComponent, NStepNumber, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetBeamMinMaxStress(
   System.int NComponent,
   System.int NStepNumber,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetBeamMinMaxStress(
   System.int NComponent,
   System.int NStepNumber,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Beam stresses as defined in [swsBeamStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBeamStressComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for static)
- `NUnits`: Stress units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of stress results for the beams

## VBA Syntax

See [CWResults::GetBeamMinMaxStress](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetBeamMinMaxStress.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetBeamForcesForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamForcesForEntities.html)
[ICWResults::GetBeamRadius Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamRadius.html)
[ICWResults::GetBeamStressForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamStressForEntities.html)

## Availability

SOLIDWORKS Simulation API 2009 SP1
