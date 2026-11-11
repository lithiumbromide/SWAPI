---
title: "IsParallelToLine Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "IsParallelToLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~IsParallelToLine.html"
---

# IsParallelToLine Method (IMathLine)

Gets whether the specified mathematical line is parallel to this mathematical line within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsParallelToLine( _
   ByVal Line As MathLine, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsParallelToLine(
   MathLine Line,
   System.double Tolerance
)
```

### JScript

```
function IsParallelToLine(
   Line : MathLine,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsParallelToLine(
   MathLine* Line,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsParallelToLine(
   MathLine^ Line,
   System.double Tolerance
)
```

### Parameters

- `Line`: [IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
- `Tolerance`: Parallel tolerance

### Return Value

True if parallel within tolerance, false if not

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
**IMathLine::IsParallelToPlane Method**
[IMathLine::IsPerpendicularToLine Method](Interop.dsAutomation~Interop.dsAutomation.IMathLine~IsPerpendicularToLine.html)

## Availability

DraftSight V1R1.4
