---
title: "GetPerimeter Method (IRegion)"
project: ""
interface: "IRegion"
member: "GetPerimeter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRegion~GetPerimeter.html"
---

# GetPerimeter Method (IRegion)

Calculates the perimeter of the Region.

## Syntax

### Visual Basic

```vb
Sub GetPerimeter( _
   ByRef Perimeter As System.Double _
)
```

### C#

```csharp
void GetPerimeter(
   out System.double Perimeter
)
```

### JScript

```
function GetPerimeter(
   Perimeter : System.double
);
```

### Managed Extensions for C++

```
void GetPerimeter(
   [PARAMFLAG::Out] System.double Perimeter
)
```

### C++/CLI

```cpp
void GetPerimeter(
   [Out] System.double Perimeter
)
```

### Parameters

- `Perimeter`: Perimeter of the Region

## Examples

[Transform Circle to Region (C#)](Transform_Circle_to_Region_Example_CSharp.htm)
[Transform Circle to Region (VB.NET)](Transform_Circle_to_Region_Example_VBNET.htm)
[Transform Circle to Region (VBA)](Transform_Circle_to_Region_Example_VBA.htm)

## See Also

[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[IRegion Members](Interop.dsAutomation~Interop.dsAutomation.IRegion_members.html)
[IRegion::GetArea Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~GetArea.html)

## Availability

DraftSight V1R2.0
