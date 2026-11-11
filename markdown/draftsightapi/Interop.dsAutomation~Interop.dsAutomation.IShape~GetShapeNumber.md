---
title: "GetShapeNumber Method (IShape)"
project: ""
interface: "IShape"
member: "GetShapeNumber"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape~GetShapeNumber.html"
---

# GetShapeNumber Method (IShape)

Gets the number of shape.

## Syntax

### Visual Basic

```vb
Function GetShapeNumber() As System.Integer
```

### C#

```csharp
System.int GetShapeNumber()
```

### JScript

```
function GetShapeNumber() : System.int;
```

### Managed Extensions for C++

```
System.int GetShapeNumber();
```

### C++/CLI

```cpp
System.int GetShapeNumber();
```

### Return Value

Code number of the shape's character with its SHX font (see **Remarks**)

## Remarks

A shape is stored as a reference to a font and to a character within that font. Essentially a shape is a single character of a compiled shape (SHX) font. This method gets the number of that character.

## See Also

[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)

## Availability

DraftSight V1R4.0
