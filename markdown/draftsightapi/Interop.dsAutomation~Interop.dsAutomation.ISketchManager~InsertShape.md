---
title: "InsertShape Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertShape"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertShape.html"
---

# InsertShape Method (ISketchManager)

Inserts a shape.

## Syntax

### Visual Basic

```vb
Function InsertShape( _
   ByVal Name As System.String, _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double, _
   ByVal Height As System.Double, _
   ByVal Rotation As System.Double _
) As Shape
```

### C#

```csharp
Shape InsertShape(
   System.string Name,
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ,
   System.double Height,
   System.double Rotation
)
```

### JScript

```
function InsertShape(
   Name : System.String,
   PositionX : System.double,
   PositionY : System.double,
   PositionZ : System.double,
   Height : System.double,
   Rotation : System.double
) : Shape;
```

### Managed Extensions for C++

```
Shape* InsertShape(
   System.string* Name,
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ,
   System.double Height,
   System.double Rotation
)
```

### C++/CLI

```cpp
Shape^ InsertShape(
   System.String^ Name,
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ,
   System.double Height,
   System.double Rotation
)
```

### Parameters

- `Name`: Name of the shape to insert (see **Remarks**)
- `PositionX`: x coordinate of the point where to insert the shape
- `PositionY`: y coordinate of the point where to insert the shape
- `PositionZ`: z coordinate of the point where to insert the shape
- `Height`: Height of the shape
- `Rotation`: Angle by which to rotate the shape

### Return Value

[Shape](Interop.dsAutomation~Interop.dsAutomation.IShape.html)

## Examples

[Insert Shapes (C#)](Insert_Shapes_Example_CSharp.htm)
[Insert Shapes (VB.NET)](Insert_Shapes_Example_VBNET.htm)
[Insert Shapes (VBA)](Insert_Shapes_Example_VBA.htm)
[Insert Shapes (JavaScript)](Insert_Shapes_Example_JS.htm)

## Remarks

A shape is stored as a reference to a font and to a character within that font. Essentially a shape is a single character of a compiled shape (SHX) font.

You must [load the shape file](Interop.dsAutomation~Interop.dsAutomation.IShapeManager~Load.html) before a shape in that file can be used in a drawing. Call [IShapeManager::GetAvailableShapes](Interop.dsAutomation~Interop.dsAutomation.IShapeManager~GetAvailableShapes.html) to get the names of shapes loaded in the drawing.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[IShapeManager::GetAvailableShapes Method ()](Interop.dsAutomation~Interop.dsAutomation.IShapeManager~GetAvailableShapes.html)

## Availability

DraftSight V1R4.0
