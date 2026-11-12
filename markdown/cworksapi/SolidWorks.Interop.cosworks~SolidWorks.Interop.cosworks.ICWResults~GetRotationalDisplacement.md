---
title: "GetRotationalDisplacement Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetRotationalDisplacement"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetRotationalDisplacement.html"
---

# GetRotationalDisplacement Method (ICWResults)

Gets the rotational displacements at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRotationalDisplacement( _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetRotationalDisplacement(NStepNumber, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetRotationalDisplacement(
   System.int NStepNumber,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetRotationalDisplacement(
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Reference geometry
- `NUnits`: Unit as defined in [swsResultsRotationalDisplacementUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsRotationalDisplacementUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of rotational displacements

## VBA Syntax

See [CWResults::GetRotationalDisplacement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetRotationalDisplacement.html).

## Remarks

Rotational degrees of freedom are available for shells and beams.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDisplacementComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementComponentForAllStepsAtNode.html)
[ICWResults::GetDisplacementForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementForEntities.html)
[ICWResults::GetMinMaxDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html)
[ICWResults::GetReactionForcesAndMoments Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetReactionForcesAndMoments.html)
[ICWResults::GetTranslationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTranslationalDisplacement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
