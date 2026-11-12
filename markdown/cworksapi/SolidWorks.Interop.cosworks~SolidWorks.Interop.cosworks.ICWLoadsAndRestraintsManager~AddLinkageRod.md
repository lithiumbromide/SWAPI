---
title: "AddLinkageRod Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddLinkageRod"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddLinkageRod.html"
---

# AddLinkageRod Method (ICWLoadsAndRestraintsManager)

Adds the specified linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLinkageRod( _
   ByVal VertexOrCircularFacesForEnd1 As System.Object, _
   ByVal VertexOrCircularFacesForEnd2 As System.Object, _
   ByVal NUnitSys As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWLinkageRod
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim VertexOrCircularFacesForEnd1 As System.Object
Dim VertexOrCircularFacesForEnd2 As System.Object
Dim NUnitSys As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWLinkageRod

value = instance.AddLinkageRod(VertexOrCircularFacesForEnd1, VertexOrCircularFacesForEnd2, NUnitSys, ErrorCode)
```

### C#

```csharp
CWLinkageRod AddLinkageRod(
   System.object VertexOrCircularFacesForEnd1,
   System.object VertexOrCircularFacesForEnd2,
   System.int NUnitSys,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWLinkageRod^ AddLinkageRod(
   System.Object^ VertexOrCircularFacesForEnd1,
   System.Object^ VertexOrCircularFacesForEnd2,
   System.int NUnitSys,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VertexOrCircularFacesForEnd1`: Array of vertex or concentric circular faces (or edges for shells) for End 1
- `VertexOrCircularFacesForEnd2`: Array of vertex or concentric circular faces (or edges for shells) for End 2
- `NUnitSys`: Units as defined by [swsUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error code as defined by [swsLinkageRodEndEditErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinkageRodEndEditErrors_e.html)

### Return Value

[ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddLinkageRod](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddLinkageRod.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
