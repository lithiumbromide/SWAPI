---
title: "AddCable Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddCable"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddCable.html"
---

# AddCable Method (ICWLoadsAndRestraintsManager)

Adds a cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCable( _
   ByVal VertexOrFaceForEnd1 As System.Object, _
   ByVal VertexOrFaceForEnd2 As System.Object, _
   ByVal NUnitSys As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWCable
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim VertexOrFaceForEnd1 As System.Object
Dim VertexOrFaceForEnd2 As System.Object
Dim NUnitSys As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWCable

value = instance.AddCable(VertexOrFaceForEnd1, VertexOrFaceForEnd2, NUnitSys, ErrorCode)
```

### C#

```csharp
CWCable AddCable(
   System.object VertexOrFaceForEnd1,
   System.object VertexOrFaceForEnd2,
   System.int NUnitSys,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWCable^ AddCable(
   System.Object^ VertexOrFaceForEnd1,
   System.Object^ VertexOrFaceForEnd2,
   System.int NUnitSys,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VertexOrFaceForEnd1`: Vertex, edge, or face for End1 (see **Remarks**)
- `VertexOrFaceForEnd2`: Vertex, edge, or face for End2 (see **Remarks**)
- `NUnitSys`: Units as defined in [swsUnitSystem_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUnitSystem_e.html)
- `ErrorCode`: Error as defined by [swsLoadsAndRestraintsErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadsAndRestraintsError_e.html)

### Return Value

[ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddCable](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddCable.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## Remarks

Specify VertexOrFaceForEnd1 and VertexOrFaceForEnd2 with one of the following objects obtained by using [IModelDocExtension::SelectByRay](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) and [ISelectionMgr::GetSelectedObject6](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html):

- Vertex
- Circular edge (for shells)
- Face or cylindrical face (for solid bodies)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::GetCable Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetCable.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
