---
title: "InsertSolid Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertSolid"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertSolid.html"
---

# InsertSolid Method (ISketchManager)

Inserts a 2D Solid, which are solid filled planes that have straight line borders, at the specified location.

## Syntax

### Visual Basic

```vb
Function InsertSolid( _
   ByVal CoordinateDblArray As System.Object _
) As Solid
```

### C#

```csharp
Solid InsertSolid(
   System.object CoordinateDblArray
)
```

### JScript

```
function InsertSolid(
   CoordinateDblArray : System.Object
) : Solid;
```

### Managed Extensions for C++

```
Solid* InsertSolid(
   System.Object* CoordinateDblArray
)
```

### C++/CLI

```cpp
Solid^ InsertSolid(
   System.Object^ CoordinateDblArray
)
```

### Parameters

- `CoordinateDblArray`: Array of doubles of the coordinates of the four vertices of corner points of the 2D Solid

### Return Value

[2D Solid](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.3
