---
title: "GetEnvelopeStrainForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetEnvelopeStrainForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetEnvelopeStrainForEntities.html"
---

# GetEnvelopeStrainForEntities Method (ICWResults)

Gets the specified envelope strain for the specified entities across all solution steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEnvelopeStrainForEntities( _
   ByVal BValueByNode As System.Boolean, _
   ByVal NComponent As System.Integer, _
   ByVal NEnvelopeType As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
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
Dim NShellFace As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetEnvelopeStrainForEntities(BValueByNode, NComponent, NEnvelopeType, DispPlane, ArraySelectedEntities, NShellFace, ErrorCode)
```

### C#

```csharp
System.object GetEnvelopeStrainForEntities(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NEnvelopeType,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NShellFace,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetEnvelopeStrainForEntities(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NEnvelopeType,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NShellFace,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BValueByNode`: True to get the strain value by node, false to get the stress value by element
- `NComponent`: Strain component as defined in [swsStrainComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrainComponent_e.html)
- `NEnvelopeType`: Envelope plot type as defined in [swsEnvelopePlotType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEnvelopePlotType_e.html)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NShellFace`: Option as defined in [swsShellFace_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellFace_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of strain component values

## VBA Syntax

See [CWResults::GetEnvelopeStrainForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetEnvelopeStrainForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
