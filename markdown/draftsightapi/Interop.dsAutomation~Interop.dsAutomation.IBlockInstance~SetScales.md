---
title: "SetScales Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "SetScales"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~SetScales.html"
---

# SetScales Method (IBlockInstance)

Sets the scale factors for the x, y, and z coordinates of the Block instance.

## Syntax

### Visual Basic

```vb
Sub SetScales( _
   ByVal ScaleX As System.Double, _
   ByVal ScaleY As System.Double, _
   ByVal ScaleZ As System.Double _
)
```

### C#

```csharp
void SetScales(
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ
)
```

### JScript

```
function SetScales(
   ScaleX : System.double,
   ScaleY : System.double,
   ScaleZ : System.double
);
```

### Managed Extensions for C++

```
void SetScales(
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ
)
```

### C++/CLI

```cpp
void SetScales(
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ
)
```

### Parameters

- `ScaleX`: Scale factor for the x coordinate
- `ScaleY`: Scale factor for the y coordinate
- `ScaleZ`: Scale factor for the z coordinate

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::GetScales Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetScales.html)

## Availability

DraftSight V1R1.1
