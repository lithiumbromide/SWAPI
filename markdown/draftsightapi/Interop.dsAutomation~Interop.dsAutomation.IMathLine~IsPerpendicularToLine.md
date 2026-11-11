---
title: "IsPerpendicularToLine Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "IsPerpendicularToLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~IsPerpendicularToLine.html"
---

# IsPerpendicularToLine Method (IMathLine)

Gets whether the specified mathematical line is perpendicular to this mathematical line within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsPerpendicularToLine( _
   ByVal Line As MathLine, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsPerpendicularToLine(
   MathLine Line,
   System.double Tolerance
)
```

### JScript

```
function IsPerpendicularToLine(
   Line : MathLine,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsPerpendicularToLine(
   MathLine* Line,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsPerpendicularToLine(
   MathLine^ Line,
   System.double Tolerance
)
```

### Parameters

- `Line`: [IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
- `Tolerance`: Perpendicular tolerance

### Return Value

True if perpendicular within tolerance, false if not

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::IsParallelToLine Method](Interop.dsAutomation~Interop.dsAutomation.IMathLine~IsParallelToLine.html)
**IMathLine::IsParallelToPlane Method**

## Availability

DraftSight V1R1.4
