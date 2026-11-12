---
title: "CreateLineByPointAndDirection Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateLineByPointAndDirection"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateLineByPointAndDirection.html"
---

# CreateLineByPointAndDirection Method (IMathUtility)

Creates a mathematical line of the specified type passing through the specified starting point in the specified direction.

## Syntax

### Visual Basic

```vb
Function CreateLineByPointAndDirection( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal Direction As MathVector, _
   ByVal Type As dsMathLineType_e _
) As MathLine
```

### C#

```csharp
MathLine CreateLineByPointAndDirection(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   MathVector Direction,
   dsMathLineType_e Type
)
```

### JScript

```
function CreateLineByPointAndDirection(
   StartX : System.double,
   StartY : System.double,
   StartZ : System.double,
   Direction : MathVector,
   Type : dsMathLineType_e
) : MathLine;
```

### Managed Extensions for C++

```
MathLine* CreateLineByPointAndDirection(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   MathVector* Direction,
   dsMathLineType_e Type
)
```

### C++/CLI

```cpp
MathLine^ CreateLineByPointAndDirection(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   MathVector^ Direction,
   dsMathLineType_e Type
)
```

### Parameters

- `StartX`: x coordinate of starting point
- `StartY`: y coordinate of starting point
- `StartZ`: z coordinate of starting point
- `Direction`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `Type`: Type of line as defined in [dsMathLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsMathLineType_e.html)

### Return Value

[IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateLine Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateLine.html)

## Availability

DraftSight V1R1.4
