---
title: "InsertMLeaderWithToleranceContentType Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertMLeaderWithToleranceContentType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithToleranceContentType.html"
---

# InsertMLeaderWithToleranceContentType Method (ISketchManager)

Inserts an MLeader in the specified location with the specified Tolerance content and attachment.

## Syntax

### Visual Basic

```vb
Function InsertMLeaderWithToleranceContentType( _
   ByVal VertexCoordinateDblArray As System.Object, _
   ByVal TolText As System.String, _
   ByVal MLeaderLineType As dsMLeaderType_e, _
   ByVal AttachmentType As dsMLeaderTolAttachmentType_e _
) As MLeader
```

### C#

```csharp
MLeader InsertMLeaderWithToleranceContentType(
   System.object VertexCoordinateDblArray,
   System.string TolText,
   dsMLeaderType_e MLeaderLineType,
   dsMLeaderTolAttachmentType_e AttachmentType
)
```

### JScript

```
function InsertMLeaderWithToleranceContentType(
   VertexCoordinateDblArray : System.Object,
   TolText : System.String,
   MLeaderLineType : dsMLeaderType_e,
   AttachmentType : dsMLeaderTolAttachmentType_e
) : MLeader;
```

### Managed Extensions for C++

```
MLeader* InsertMLeaderWithToleranceContentType(
   System.Object* VertexCoordinateDblArray,
   System.string* TolText,
   dsMLeaderType_e MLeaderLineType,
   dsMLeaderTolAttachmentType_e AttachmentType
)
```

### C++/CLI

```cpp
MLeader^ InsertMLeaderWithToleranceContentType(
   System.Object^ VertexCoordinateDblArray,
   System.String^ TolText,
   dsMLeaderType_e MLeaderLineType,
   dsMLeaderTolAttachmentType_e AttachmentType
)
```

### Parameters

- `VertexCoordinateDblArray`: Location array of x, y, and z coordinates specifying the start point and interior vertexes of MLeader (see **Remarks**)
- `TolText`: Tolerance text
- `MLeaderLineType`: Type of MLeader line as defined by [dsMLeaderType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderType_e.html)
- `AttachmentType`: Type of tolerance attachment as defined by [dsMLeaderTolAttachmentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderTolAttachmentType_e.html)

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
[ISketchManager::InsertMLeaderWithNoneContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoneContentType.html)
[ISketchManager::InsertMLeaderWithNoteContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html)

## Availability

DraftSight 2024 SP4
