---
title: "InsertLeader Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertLeader"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertLeader.html"
---

# InsertLeader Method (ISketchManager)

Inserts a Leader.

## Syntax

### Visual Basic

```vb
Function InsertLeader( _
   ByVal VertexCoordinateDblArray As System.Object, _
   ByVal NoteWidth As System.Double, _
   ByVal NoteText As System.String _
) As Leader
```

### C#

```csharp
Leader InsertLeader(
   System.object VertexCoordinateDblArray,
   System.double NoteWidth,
   System.string NoteText
)
```

### JScript

```
function InsertLeader(
   VertexCoordinateDblArray : System.Object,
   NoteWidth : System.double,
   NoteText : System.String
) : Leader;
```

### Managed Extensions for C++

```
Leader* InsertLeader(
   System.Object* VertexCoordinateDblArray,
   System.double NoteWidth,
   System.string* NoteText
)
```

### C++/CLI

```cpp
Leader^ InsertLeader(
   System.Object^ VertexCoordinateDblArray,
   System.double NoteWidth,
   System.String^ NoteText
)
```

### Parameters

- `VertexCoordinateDblArray`: Array of x, y, and z coordinates indicating the start point for the Leader and the segment vertices to define the Leader (see **Remarks**)
- `NoteWidth`: Width of Note
- `NoteText`: Note text (see **Remarks**)

### Return Value

[Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)

## Examples

[Create Aligned Linear and Ordinate Dimensions (C#)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm)
[Create Aligned Linear and Ordinate Dimensions (VB.NET)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm)
[Create Aligned Linear and Ordinate Dimensions (VBA)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm)
[Attach Block Definition Annotation to Leader (C#)](Attach_Block_Definition_Annotation_to_Leader_Example_CSharp.htm)
[Attach Block Definition Annotation to Leader (VB.NET)](Attach_Block_Definition_Annotation_to_Leader_Example_VBNET.htm)
[Attach Block Definition Annotation to Leader (VBA)](Attach_Block_Definition_Annotation_to_Leader_Example_VBA.htm)
[Attach Block Definition Annotation to Leader (JavaScript)](Attach_Block_Definition_Annotation_to_Leader_Example_JS.htm)

## Remarks

The size of VertexCoordinateDblArray is (3 * (Number of vertices)). The order of the elements in the array is (x1, y1, z1, x2, y2, z2...).

The x1, y1, and z1 coordinates in the array represent the start point; all subsequent x`n`, y`n`, and z`n` coordinates represent segment vertices.

The NoteText parameter is ignored when the leader is created in temporary mode.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertMLeaderWithBlockContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html)
[ISketchManager::InsertMLeaderWithNoneContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoneContentType.html)
[ISketchManager::InsertMLeaderWithNoteContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html)
[ISketchManager::InsertMLeaderWithToleranceContentType Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithToleranceContentType.html)

## Availability

DraftSight V1R1.2
