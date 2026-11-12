---
title: "GetEdgeType Method (IHatchBoundaryLoop)"
project: ""
interface: "IHatchBoundaryLoop"
member: "GetEdgeType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgeType.html"
---

# GetEdgeType Method (IHatchBoundaryLoop)

Gets the type of the specified Hatch boundary edge.

## Syntax

### Visual Basic

```vb
Function GetEdgeType( _
   ByVal Index As System.Integer _
) As dsHatchEdgeType_e
```

### C#

```csharp
dsHatchEdgeType_e GetEdgeType(
   System.int Index
)
```

### JScript

```
function GetEdgeType(
   Index : System.int
) : dsHatchEdgeType_e;
```

### Managed Extensions for C++

```
dsHatchEdgeType_e GetEdgeType(
   System.int Index
)
```

### C++/CLI

```cpp
dsHatchEdgeType_e GetEdgeType(
   System.int Index
)
```

### Parameters

- `Index`: Index of the Hatch boundary edge (see **Remarks**)

### Return Value

Type of Hatch boundary edge as defined in [dsHatchEdgeType_e](Interop.dsAutomation~Interop.dsAutomation.dsHatchEdgeType_e.html)

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

Before calling this method, call [IHatchBoundaryLoop::GetEdgesCount](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgesCount.html) to determine a valid value for Index.

## See Also

[IHatchBoundaryLoop Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)
[IHatchBoundaryLoop Members](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop_members.html)

## Availability

DraftSight V1R1.3
