---
title: "InsertPolyline2D Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPolyline2D"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyline2D.html"
---

# InsertPolyline2D Method (ISketchManager)

Constructs a 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function InsertPolyline2D( _
   ByVal CoordinateDblArray As System.Object, _
   ByVal Closed As System.Boolean _
) As PolyLine
```

### C#

```csharp
PolyLine InsertPolyline2D(
   System.object CoordinateDblArray,
   System.bool Closed
)
```

### JScript

```
function InsertPolyline2D(
   CoordinateDblArray : System.Object,
   Closed : System.boolean
) : PolyLine;
```

### Managed Extensions for C++

```
PolyLine* InsertPolyline2D(
   System.Object* CoordinateDblArray,
   System.bool Closed
)
```

### C++/CLI

```cpp
PolyLine^ InsertPolyline2D(
   System.Object^ CoordinateDblArray,
   System.bool Closed
)
```

### Parameters

- `CoordinateDblArray`: Array of the x, y coordinates of the 2D PolyLine (see **Remarks**)
- `Closed`: True to close the 2D PolyLine, false to leave it open

### Return Value

[2D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)

## Examples

[Construct 2D PolyLine (C#)](Construct_2D_PolyLine_Example_CSharp.htm)
[Construct 2D PolyLine (VB.NET)](Construct_2D_PolyLine_Example_VBNET.htm)
[Construct 2D PolyLine (VBA)](Construct_2D_PolyLine_Example_VBA.htm)
[Create Aligned Linear and Ordinate Dimensions (C#)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm)
[Create Aligned Linear and Ordinate Dimensions (VB.NET)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm)
[Create Aligned Linear and Ordinate Dimensions (VBA)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)

## Remarks

The size of CoordinateDblArray is (2 * (Number of 2D PolyLine vertices)). The order of the elements in the array is (x1, y1, x2, y2, ...).

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPolyline3D Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyline3D.html)

## Availability

DraftSight V1R1.1
