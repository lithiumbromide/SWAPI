---
title: "GetStressForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStressForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressForEntities.html"
---

# GetStressForEntities Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetStressForEntities2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetStressForEntities2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStressForEntities( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArrayArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArrayArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStressForEntities(NComponent, NStepNumber, DispPlane, ArrayArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetStressForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArrayArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStressForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArrayArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Stress as defined in [swsStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStressComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for steady state)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArrayArraySelectedEntities`: Array of geometric entities
- `NUnits`: Unit as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of stress results

## VBA Syntax

See [CWResults::GetStressForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStressForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html)
[ICWResults::GetStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStress.html)
[ICWResults::GetStressComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressComponentForAllStepsAtNode.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
