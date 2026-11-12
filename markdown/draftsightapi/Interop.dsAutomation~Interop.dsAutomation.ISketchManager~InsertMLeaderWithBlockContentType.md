---
title: "InsertMLeaderWithBlockContentType Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertMLeaderWithBlockContentType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html"
---

# InsertMLeaderWithBlockContentType Method (ISketchManager)

Inserts an MLeader in the specified location with the specified Block name.

## Syntax

### Visual Basic

```vb
Function InsertMLeaderWithBlockContentType( _
   ByVal VertexCoordinateDblArray As System.Object, _
   ByVal BlockName As System.String, _
   ByVal MLeaderLineType As dsMLeaderType_e _
) As MLeader
```

### C#

```csharp
MLeader InsertMLeaderWithBlockContentType(
   System.object VertexCoordinateDblArray,
   System.string BlockName,
   dsMLeaderType_e MLeaderLineType
)
```

### JScript

```
function InsertMLeaderWithBlockContentType(
   VertexCoordinateDblArray : System.Object,
   BlockName : System.String,
   MLeaderLineType : dsMLeaderType_e
) : MLeader;
```

### Managed Extensions for C++

```
MLeader* InsertMLeaderWithBlockContentType(
   System.Object* VertexCoordinateDblArray,
   System.string* BlockName,
   dsMLeaderType_e MLeaderLineType
)
```

### C++/CLI

```cpp
MLeader^ InsertMLeaderWithBlockContentType(
   System.Object^ VertexCoordinateDblArray,
   System.String^ BlockName,
   dsMLeaderType_e MLeaderLineType
)
```

### Parameters

- `VertexCoordinateDblArray`: Location array of x, y, and z coordinates specifying the start point and interior vertexes of the MLeader (see **Remarks**)
- `BlockName`: Name of Block to create
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
[ISketchManager::InsertMLeaderWithNoneContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoneContentType.html)
[ISketchManager::InsertMLeaderWithNoteContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html)
[ISketchManager::InsertMLeaderWithToleranceContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithToleranceContentType.html)

## Availability

DraftSight 2024 SP4
