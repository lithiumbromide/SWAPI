---
title: "GetEnvelopeAccelerationForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetEnvelopeAccelerationForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetEnvelopeAccelerationForEntities.html"
---

# GetEnvelopeAccelerationForEntities Method (ICWResults)

Gets the specified envelope acceleration for the specified entities across all solution steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEnvelopeAccelerationForEntities( _
   ByVal NComponent As System.Integer, _
   ByVal NEnvelopeType As System.Integer, _
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
Dim NEnvelopeType As System.Integer
Dim DispPlane As System.Object
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetEnvelopeAccelerationForEntities(NComponent, NEnvelopeType, DispPlane, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetEnvelopeAccelerationForEntities(
   System.int NComponent,
   System.int NEnvelopeType,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetEnvelopeAccelerationForEntities(
   System.int NComponent,
   System.int NEnvelopeType,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Component of acceleration as defined in [swsAccelerationComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationComponent_e.html)
- `NEnvelopeType`: Envelope plot type as defined in [swsEnvelopePlotType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEnvelopePlotType_e.html)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Units of acceleration as defined by [swsAccelerationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of acceleration component values

## VBA Syntax

See [CWResults::GetEnvelopeAccelerationForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetEnvelopeAccelerationForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
