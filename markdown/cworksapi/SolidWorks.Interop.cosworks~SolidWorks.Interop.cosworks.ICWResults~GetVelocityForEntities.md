---
title: "GetVelocityForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetVelocityForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetVelocityForEntities.html"
---

# GetVelocityForEntities Method (ICWResults)

Gets the specified velocity component for the specified entities and at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVelocityForEntities( _
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

value = instance.GetVelocityForEntities(NComponent, NStepNumber, DispPlane, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetVelocityForEntities(
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
System.Object^ GetVelocityForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Velocity component as defined in [swsVelocityComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsVelocityComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for steady state)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Units of velocity as defined in [swsVelocityUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsVelocityUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWResults::GetVelocityForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetVelocityForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
