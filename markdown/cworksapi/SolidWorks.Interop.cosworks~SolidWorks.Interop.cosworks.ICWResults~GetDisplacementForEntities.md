---
title: "GetDisplacementForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDisplacementForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementForEntities.html"
---

# GetDisplacementForEntities Method (ICWResults)

Gets the specified displacement component for the specified entities at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplacementForEntities( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
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
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetDisplacementForEntities(NComponent, NStepNumber, DispPlane, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetDisplacementForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetDisplacementForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Displacement component as defined in [swsDisplacementComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDisplacementComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Linear units for displacement translation as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of displacement component values

## VBA Syntax

See [CWResults::GetDisplacementForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDisplacementForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDisplacementComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementComponentForAllStepsAtNode.html)
[ICWResults::GetMinMaxDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html)
[ICWResults::GetTranslationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTranslationalDisplacement.html)
[ICWResults::GetReactionForcesAndMoments Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetReactionForcesAndMoments.html)
[ICWResults::GetRotationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetRotationalDisplacement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
