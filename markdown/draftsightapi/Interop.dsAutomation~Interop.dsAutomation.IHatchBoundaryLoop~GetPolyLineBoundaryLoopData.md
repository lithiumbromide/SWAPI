---
title: "GetPolyLineBoundaryLoopData Method (IHatchBoundaryLoop)"
project: ""
interface: "IHatchBoundaryLoop"
member: "GetPolyLineBoundaryLoopData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetPolyLineBoundaryLoopData.html"
---

# GetPolyLineBoundaryLoopData Method (IHatchBoundaryLoop)

Gets the PolyLine data for the Hatch boundary.

## Syntax

### Visual Basic

```vb
Sub GetPolyLineBoundaryLoopData( _
   ByRef HasBulge As System.Boolean, _
   ByRef IsClosed As System.Boolean, _
   ByRef CoordinateDblArray As System.Object, _
   ByRef BulgesDblArray As System.Object _
)
```

### C#

```csharp
void GetPolyLineBoundaryLoopData(
   out System.bool HasBulge,
   out System.bool IsClosed,
   out System.object CoordinateDblArray,
   out System.object BulgesDblArray
)
```

### JScript

```
function GetPolyLineBoundaryLoopData(
   HasBulge : System.boolean,
   IsClosed : System.boolean,
   CoordinateDblArray : System.Object,
   BulgesDblArray : System.Object
);
```

### Managed Extensions for C++

```
void GetPolyLineBoundaryLoopData(
   [PARAMFLAG::Out] System.bool HasBulge,
   [PARAMFLAG::Out] System.bool IsClosed,
   [PARAMFLAG::Out] System.Object* CoordinateDblArray,
   [PARAMFLAG::Out] System.Object* BulgesDblArray
)
```

### C++/CLI

```cpp
void GetPolyLineBoundaryLoopData(
   [Out] System.bool HasBulge,
   [Out] System.bool IsClosed,
   [Out] System.Object^ CoordinateDblArray,
   [Out] System.Object^ BulgesDblArray
)
```

### Parameters

- `HasBulge`: True if the PolyLine has bulge, false if not
- `IsClosed`: True if the PolyLine is closed, false if not
- `CoordinateDblArray`: Array of doubles of the PolyLine coordinates
- `BulgesDblArray`: Array of doubles of the bulge coordinates

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

This method is valid only when [IHatchBoundaryLoop::IsPolyLine](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~IsPolyLine.html) is true.

## See Also

[IHatchBoundaryLoop Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)
[IHatchBoundaryLoop Members](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop_members.html)
