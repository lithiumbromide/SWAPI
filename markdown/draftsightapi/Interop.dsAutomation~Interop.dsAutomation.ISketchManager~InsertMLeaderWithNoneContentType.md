---
title: "InsertMLeaderWithNoneContentType Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertMLeaderWithNoneContentType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoneContentType.html"
---

# InsertMLeaderWithNoneContentType Method (ISketchManager)

Inserts an MLeader in the specified location.

## Syntax

### Visual Basic

```vb
Function InsertMLeaderWithNoneContentType( _
   ByVal VertexCoordinateDblArray As System.Object, _
   ByVal MLeaderLineType As dsMLeaderType_e _
) As MLeader
```

### C#

```csharp
MLeader InsertMLeaderWithNoneContentType(
   System.object VertexCoordinateDblArray,
   dsMLeaderType_e MLeaderLineType
)
```

### JScript

```
function InsertMLeaderWithNoneContentType(
   VertexCoordinateDblArray : System.Object,
   MLeaderLineType : dsMLeaderType_e
) : MLeader;
```

### Managed Extensions for C++

```
MLeader* InsertMLeaderWithNoneContentType(
   System.Object* VertexCoordinateDblArray,
   dsMLeaderType_e MLeaderLineType
)
```

### C++/CLI

```cpp
MLeader^ InsertMLeaderWithNoneContentType(
   System.Object^ VertexCoordinateDblArray,
   dsMLeaderType_e MLeaderLineType
)
```

### Parameters

- `VertexCoordinateDblArray`: Location array of x, y, and z coordinates specifying the start point and interior vertexes of MLeader (see **Remarks**)
- `MLeaderLineType`: Type of MLeader line as defined by [dsMLeaderType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderType_e.html)

### Return Value

[IMLeader](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)

## Examples

See the IMLeader example.

## Remarks

The size of VertexCoordinateDblArray is (3 * (`number_of_MLeader_vertices`)). The order of the elements in the array is (x1, y1, z1, x2, y2, z2...).

The x1, y1, and z1 coordinates in the array represent the start point of the MLeader; all subsequent x`n`, y`n`, and z`n` coordinates represent the MLeader's interior vertices.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertLeader Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertLeader.html)
[ISketchManager::InsertMLeaderWithBlockContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html)
[ISketchManager::InsertMLeaderWithNoteContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html)
[ISketchManager::InsertMLeaderWithToleranceContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithToleranceContentType.html)

## Availability

DraftSight 2024 SP4
