---
title: "GetEnvelopeDisplacementForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetEnvelopeDisplacementForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetEnvelopeDisplacementForEntities.html"
---

# GetEnvelopeDisplacementForEntities Method (ICWResults)

Gets the specified envelope displacement for the specified entities across all solution steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEnvelopeDisplacementForEntities( _
   ByVal BValueByNode As System.Boolean, _
   ByVal NComponent As System.Integer, _
   ByVal NEnvelopeType As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal NShellFace As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BValueByNode As System.Boolean
Dim NComponent As System.Integer
Dim NEnvelopeType As System.Integer
Dim DispPlane As System.Object
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim NShellFace As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetEnvelopeDisplacementForEntities(BValueByNode, NComponent, NEnvelopeType, DispPlane, ArraySelectedEntities, NUnits, NShellFace, ErrorCode)
```

### C#

```csharp
System.object GetEnvelopeDisplacementForEntities(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NEnvelopeType,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NUnits,
   System.int NShellFace,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetEnvelopeDisplacementForEntities(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NEnvelopeType,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   System.int NShellFace,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BValueByNode`: True to get the displacement value by node, false to get the stress value by element
- `NComponent`: Displacement component as defined in [swsDisplacementComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDisplacementComponent_e.html)
- `NEnvelopeType`: Envelope plot type as defined in [swsEnvelopePlotType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEnvelopePlotType_e.html)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Linear units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `NShellFace`: Option as defined in [swsShellFace_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellFace_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of displacement component values

## VBA Syntax

See [CWResults::GetEnvelopeDisplacementForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetEnvelopeDisplacementForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
