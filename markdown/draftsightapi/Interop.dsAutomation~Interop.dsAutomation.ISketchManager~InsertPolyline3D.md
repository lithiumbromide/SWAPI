---
title: "InsertPolyline3D Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPolyline3D"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyline3D.html"
---

# InsertPolyline3D Method (ISketchManager)

Constructs a 3D PolyLine.

## Syntax

### Visual Basic

```vb
Function InsertPolyline3D( _
   ByVal CoordinateDblArray As System.Object, _
   ByVal Closed As System.Boolean _
) As PolyLine3D
```

### C#

```csharp
PolyLine3D InsertPolyline3D(
   System.object CoordinateDblArray,
   System.bool Closed
)
```

### JScript

```
function InsertPolyline3D(
   CoordinateDblArray : System.Object,
   Closed : System.boolean
) : PolyLine3D;
```

### Managed Extensions for C++

```
PolyLine3D* InsertPolyline3D(
   System.Object* CoordinateDblArray,
   System.bool Closed
)
```

### C++/CLI

```cpp
PolyLine3D^ InsertPolyline3D(
   System.Object^ CoordinateDblArray,
   System.bool Closed
)
```

### Parameters

- `CoordinateDblArray`: Array of the x, y, and z coordinates of the 3D PolyLine (see **Remarks**)
- `Closed`: True to close the 3D PolyLine, false to leave it open

### Return Value

[IPolyLine3D](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)

## Remarks

The size of CoordinateDblArray is (3 * (Number of 3D PolyLine vertices)). The order of the elements in the array is (x1, y1, z1, x2, y2, z2 ...).

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPolyline2D Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyline2D.html)

## Availability

DraftSight V1R1.3
