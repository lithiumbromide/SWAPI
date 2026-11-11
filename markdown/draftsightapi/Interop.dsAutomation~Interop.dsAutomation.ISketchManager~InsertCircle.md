---
title: "InsertCircle Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertCircle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircle.html"
---

# InsertCircle Method (ISketchManager)

Constructs a Circle.

## Syntax

### Visual Basic

```vb
Function InsertCircle( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal Radius As System.Double _
) As Circle
```

### C#

```csharp
Circle InsertCircle(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Radius
)
```

### JScript

```
function InsertCircle(
   CenterX : System.double,
   CenterY : System.double,
   CenterZ : System.double,
   Radius : System.double
) : Circle;
```

### Managed Extensions for C++

```
Circle* InsertCircle(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Radius
)
```

### C++/CLI

```cpp
Circle^ InsertCircle(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Radius
)
```

### Parameters

- `CenterX`: x coordinate for the center point of the Circle
- `CenterY`: y coordinate for the center point of the Circle
- `CenterZ`: z coordinate for the center point of the Circle
- `Radius`: Radius of Circle

### Return Value

[Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)

## Examples

[Construct Circle (C#)](Construct_Circle_Example_CSharp.htm)
[Construct Circle (VB.NET)](Construct_Circle_Example_VBNET.htm)
[Construct Circle (VBA)](Construct_Circle_Example_VBA.htm)
[Create Aligned Linear and Ordinate Dimensions (C#)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm)
[Create Aligned Linear and Ordinate Dimensions (VB.NET)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm)
[Create Aligned Linear and Ordinate Dimensions (VBA)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertCircleBy3Points Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleBy3Points.html)
[ISketchManager::InsertCircleByDiameter Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleByDiameter.html)

## Availability

DraftSight V1R1.1
