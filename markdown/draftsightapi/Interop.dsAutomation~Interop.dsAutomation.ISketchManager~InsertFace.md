---
title: "InsertFace Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertFace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertFace.html"
---

# InsertFace Method (ISketchManager)

Inserts a Face.

## Syntax

### Visual Basic

```vb
Function InsertFace( _
   ByVal CoordinateDblArray As System.Object, _
   ByVal Edge1Visible As System.Boolean, _
   ByVal Edge2Visible As System.Boolean, _
   ByVal Edge3Visible As System.Boolean, _
   ByVal Edge4Visible As System.Boolean _
) As Face
```

### C#

```csharp
Face InsertFace(
   System.object CoordinateDblArray,
   System.bool Edge1Visible,
   System.bool Edge2Visible,
   System.bool Edge3Visible,
   System.bool Edge4Visible
)
```

### JScript

```
function InsertFace(
   CoordinateDblArray : System.Object,
   Edge1Visible : System.boolean,
   Edge2Visible : System.boolean,
   Edge3Visible : System.boolean,
   Edge4Visible : System.boolean
) : Face;
```

### Managed Extensions for C++

```
Face* InsertFace(
   System.Object* CoordinateDblArray,
   System.bool Edge1Visible,
   System.bool Edge2Visible,
   System.bool Edge3Visible,
   System.bool Edge4Visible
)
```

### C++/CLI

```cpp
Face^ InsertFace(
   System.Object^ CoordinateDblArray,
   System.bool Edge1Visible,
   System.bool Edge2Visible,
   System.bool Edge3Visible,
   System.bool Edge4Visible
)
```

### Parameters

- `CoordinateDblArray`: Array of doubles of the coordinates of the Face to insert
- `Edge1Visible`: True to show first edge, false to not
- `Edge2Visible`: True to show second edge, false to not
- `Edge3Visible`: True to show third edge, false to not
- `Edge4Visible`: True to show fourth edge, false to not

### Return Value

[Face](Interop.dsAutomation~Interop.dsAutomation.IFace.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.3
