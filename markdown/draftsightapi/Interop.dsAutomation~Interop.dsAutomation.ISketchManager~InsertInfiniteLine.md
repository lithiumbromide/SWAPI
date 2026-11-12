---
title: "InsertInfiniteLine Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertInfiniteLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertInfiniteLine.html"
---

# InsertInfiniteLine Method (ISketchManager)

Constructs an InfiniteLine.

## Syntax

### Visual Basic

```vb
Function InsertInfiniteLine( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As InfiniteLine
```

### C#

```csharp
InfiniteLine InsertInfiniteLine(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### JScript

```
function InsertInfiniteLine(
   X1 : System.double,
   Y1 : System.double,
   Z1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Z2 : System.double
) : InfiniteLine;
```

### Managed Extensions for C++

```
InfiniteLine* InsertInfiniteLine(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
InfiniteLine^ InsertInfiniteLine(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### Parameters

- `X1`: x coordinate of the central position of the InfiniteLine
- `Y1`: y coordinate of the central position of the InfiniteLine
- `Z1`: z coordinate of the central position of the InfiniteLine
- `X2`: x coordinate of the through point that defines the direction of the InfiniteLine
- `Y2`: y coordinate of the through point that defines the direction of the InfiniteLine
- `Z2`: z coordinate of the through point that defines the direction of the InfiniteLine

### Return Value

[InfiniteLine](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)

## Examples

[Construct InfiniteLine (C#)](Construct_InfiniteLine_Example_CSharp.htm)
[Construct InfiniteLine (VB.NET)](Construct_InfiniteLine_Example_VBNET.htm)
[Construct InfiniteLine (VBA)](Construct_InfiniteLine_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.1
