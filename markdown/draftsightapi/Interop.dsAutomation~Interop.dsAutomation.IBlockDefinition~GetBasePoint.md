---
title: "GetBasePoint Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "GetBasePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetBasePoint.html"
---

# GetBasePoint Method (IBlockDefinition)

Gets the coordinates of the base point of this Block definition.

## Syntax

### Visual Basic

```vb
Sub GetBasePoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetBasePoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetBasePoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetBasePoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetBasePoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IBlockDefinition::SetBasePoint Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~SetBasePoint.html)

## Availability

DraftSight V1R1.4
