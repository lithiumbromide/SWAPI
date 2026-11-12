---
title: "InsertRay Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertRay"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRay.html"
---

# InsertRay Method (ISketchManager)

Inserts a Ray.

## Syntax

### Visual Basic

```vb
Function InsertRay( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal ThroughX As System.Double, _
   ByVal ThroughY As System.Double, _
   ByVal ThroughZ As System.Double _
) As Ray
```

### C#

```csharp
Ray InsertRay(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double ThroughX,
   System.double ThroughY,
   System.double ThroughZ
)
```

### JScript

```
function InsertRay(
   StartX : System.double,
   StartY : System.double,
   StartZ : System.double,
   ThroughX : System.double,
   ThroughY : System.double,
   ThroughZ : System.double
) : Ray;
```

### Managed Extensions for C++

```
Ray* InsertRay(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double ThroughX,
   System.double ThroughY,
   System.double ThroughZ
)
```

### C++/CLI

```cpp
Ray^ InsertRay(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double ThroughX,
   System.double ThroughY,
   System.double ThroughZ
)
```

### Parameters

- `StartX`: x coordinate of the base (start) point of the Ray
- `StartY`: y coordinate of the base point of the Ray
- `StartZ`: z coordinate of the base point of the Ray
- `ThroughX`: x coordinate of the through point (point that defines the direction of the Ray from the base point) for the Ray
- `ThroughY`: y coordinate of the through point for the Ray
- `ThroughZ`: z coordinate of the through point for the Ray

### Return Value

[Ray](Interop.dsAutomation~Interop.dsAutomation.IRay.html)

## Examples

[Insert Ray (C#)](Insert_Ray_Example_CSharp.htm)
[Insert Ray (VB.NET)](Insert_Ray_Example_VBNET.htm)
[Insert Ray (VBA)](Insert_Ray_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.1
