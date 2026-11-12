---
title: "GetHatchBoundaryLoop Method (IHatch)"
project: ""
interface: "IHatch"
member: "GetHatchBoundaryLoop"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~GetHatchBoundaryLoop.html"
---

# GetHatchBoundaryLoop Method (IHatch)

Gets the specified Hatch boundary loop.

## Syntax

### Visual Basic

```vb
Function GetHatchBoundaryLoop( _
   ByVal Index As System.Integer _
) As HatchBoundaryLoop
```

### C#

```csharp
HatchBoundaryLoop GetHatchBoundaryLoop(
   System.int Index
)
```

### JScript

```
function GetHatchBoundaryLoop(
   Index : System.int
) : HatchBoundaryLoop;
```

### Managed Extensions for C++

```
HatchBoundaryLoop* GetHatchBoundaryLoop(
   System.int Index
)
```

### C++/CLI

```cpp
HatchBoundaryLoop^ GetHatchBoundaryLoop(
   System.int Index
)
```

### Parameters

- `Index`: Index of the Hatch boundary loop to get (see **Remarks**)

### Return Value

[IHatchBoundaryLoop](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

Before calling this method, call [IHatch::GetHatchBoundaryLoopsCount](Interop.dsAutomation~Interop.dsAutomation.IHatch~GetBoundaryLoopsCount.html) to determine a valid value for index.

## See Also

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)
[IHatch::GetBoundaryLoopsCount Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~GetBoundaryLoopsCount.html)

## Availability

DraftSight V1R1.3
