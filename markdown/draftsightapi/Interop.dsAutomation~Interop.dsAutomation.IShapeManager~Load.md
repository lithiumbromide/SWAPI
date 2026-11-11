---
title: "Load Method (IShapeManager)"
project: ""
interface: "IShapeManager"
member: "Load"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShapeManager~Load.html"
---

# Load Method (IShapeManager)

Loads the compiled shape file, using the specified path and file name, in the drawing.

## Syntax

### Visual Basic

```vb
Sub Load( _
   ByVal PathName As System.String _
)
```

### C#

```csharp
void Load(
   System.string PathName
)
```

### JScript

```
function Load(
   PathName : System.String
);
```

### Managed Extensions for C++

```
void Load(
   System.string* PathName
)
```

### C++/CLI

```cpp
void Load(
   System.String^ PathName
)
```

### Parameters

- `PathName`: Path and file name of the compiled shape file to load in the drawing

## Examples

[Insert Shapes (C#)](Insert_Shapes_Example_CSharp.htm)
[Insert Shapes (VB.NET)](Insert_Shapes_Example_VBNET.htm)
[Insert Shapes (VBA)](Insert_Shapes_Example_VBA.htm)
[Insert Shapes (JavaScript)](Insert_Shapes_Example_JS.htm)

## Remarks

The filename extension of a shape file is **.shx**, and the file is a compiled shape file.

## See Also

[IShapeManager Interface](Interop.dsAutomation~Interop.dsAutomation.IShapeManager.html)
[IShapeManager Members](Interop.dsAutomation~Interop.dsAutomation.IShapeManager_members.html)
[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)

## Availability

DraftSight V1R4.0
