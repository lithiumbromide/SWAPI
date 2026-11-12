---
title: "GetScales Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "GetScales"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetScales.html"
---

# GetScales Method (IBlockInstance)

Gets the scale factors for the x, y, and z coordinates of the Block instance.

## Syntax

### Visual Basic

```vb
Sub GetScales( _
   ByRef ScaleX As System.Double, _
   ByRef ScaleY As System.Double, _
   ByRef ScaleZ As System.Double _
)
```

### C#

```csharp
void GetScales(
   out System.double ScaleX,
   out System.double ScaleY,
   out System.double ScaleZ
)
```

### JScript

```
function GetScales(
   ScaleX : System.double,
   ScaleY : System.double,
   ScaleZ : System.double
);
```

### Managed Extensions for C++

```
void GetScales(
   [PARAMFLAG::Out] System.double ScaleX,
   [PARAMFLAG::Out] System.double ScaleY,
   [PARAMFLAG::Out] System.double ScaleZ
)
```

### C++/CLI

```cpp
void GetScales(
   [Out] System.double ScaleX,
   [Out] System.double ScaleY,
   [Out] System.double ScaleZ
)
```

### Parameters

- `ScaleX`: Scale factor for the x coordinate
- `ScaleY`: Scale factor for the y coordinate
- `ScaleZ`: Scale factor for the z coordinate

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::SetScales Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~SetScales.html)

## Availability

DraftSight V1R1.1
