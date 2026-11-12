---
title: "GetBoundingBox Method (IHatch)"
project: ""
interface: "IHatch"
member: "GetBoundingBox"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~GetBoundingBox.html"
---

# GetBoundingBox Method (IHatch)

Gets the bounding box enclosing the Hatch.

## Syntax

### Visual Basic

```vb
Sub GetBoundingBox( _
   ByRef X1 As System.Double, _
   ByRef Y1 As System.Double, _
   ByRef Z1 As System.Double, _
   ByRef X2 As System.Double, _
   ByRef Y2 As System.Double, _
   ByRef Z2 As System.Double _
)
```

### C#

```csharp
void GetBoundingBox(
   out System.double X1,
   out System.double Y1,
   out System.double Z1,
   out System.double X2,
   out System.double Y2,
   out System.double Z2
)
```

### JScript

```
function GetBoundingBox(
   X1 : System.double,
   Y1 : System.double,
   Z1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Z2 : System.double
);
```

### Managed Extensions for C++

```
void GetBoundingBox(
   [PARAMFLAG::Out] System.double X1,
   [PARAMFLAG::Out] System.double Y1,
   [PARAMFLAG::Out] System.double Z1,
   [PARAMFLAG::Out] System.double X2,
   [PARAMFLAG::Out] System.double Y2,
   [PARAMFLAG::Out] System.double Z2
)
```

### C++/CLI

```cpp
void GetBoundingBox(
   [Out] System.double X1,
   [Out] System.double Y1,
   [Out] System.double Z1,
   [Out] System.double X2,
   [Out] System.double Y2,
   [Out] System.double Z2
)
```

### Parameters

- `X1`: x coordinate of a corner of the bounding box
- `Y1`: y coordinate of a corner of the bounding box
- `Z1`: z coordinate of a corner of the bounding box
- `X2`: x coordinate of the opposite diagonal corner of the bounding box
- `Y2`: y coordinate of the opposite diagonal corner of the bounding box
- `Z2`: z coordinate of the opposite diagonal corner of the bounding box

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Bounary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## See Also

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)

## Availability

DraftSight V1R1.3
