---
title: "IShape Interface"
project: ""
interface: "IShape"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape.html"
---

# IShape Interface

Allows access to a shape.

## Syntax

### Visual Basic

```vb
Public Interface IShape
```

### C#

```csharp
public interface IShape
```

### JScript

```
public interface IShape
```

### Managed Extensions for C++

```
public __gc __interface IShape
```

### C++/CLI

```cpp
public interface class IShape
```

## Examples

[Insert Shapes (C#)](Insert_Shapes_Example_CSharp.htm)
[Insert Shapes (VB.NET)](Insert_Shapes_Example_VBNET.htm)
[Insert Shapes (VBA)](Insert_Shapes_Example_VBA.htm)
[Insert Shapes (JavaScript)](Insert_Shapes_Example_JS.htm)

## Remarks

A shape is stored as a reference to a font and to a character within that font. Essentially a shape is a single character of a compiled shape (SHX) font.

You must [load the shape file](Interop.dsAutomation~Interop.dsAutomation.IShapeManager~Load.html) before a shape in that file can be used in a drawing.

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::InsertShape](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertShape.html)

## Access Diagram

DSObjectModel.pdf#Shape

[Shape](DSObjectModel.pdf#Shape)

## See Also

[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IShapeManager Interface](Interop.dsAutomation~Interop.dsAutomation.IShapeManager.html)
[IDrawingSupportFiles::AlternateBigFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateBigFontFile.html)
[IDrawingSupportFiles::AlternateShapeFile ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShapeFile.html)
[IDrawingSupportFiles::AlternateShxFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShxFontFile.html)
