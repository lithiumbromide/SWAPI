---
title: "MathLine Property (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "MathLine"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~MathLine.html"
---

# MathLine Property (IInfiniteLine)

Gets a mathematical line that is derived from this InfiniteLine or sets the first and second points of this InfiniteLine using the specified mathematical line.

## Syntax

### Visual Basic

```vb
Property MathLine As MathLine
```

### C#

```csharp
MathLine MathLine {get; set;}
```

### JScript

```
function get,set MathLine : MathLine
```

### Managed Extensions for C++

```
__property MathLine* get_MathLine();
__property void set_MathLine(
   MathLine* value
);
```

### C++/CLI

```cpp
property MathLine^ MathLine {
   MathLine^ get();
   void set (    MathLine^ value);
}
```

### Property Value

[IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html) (see **Remarks**)

## Remarks

The get property returns a new mathematical line of type [dsMathLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsMathLineType_e.html).dsMathLineType_Infinite. The coordinates of the starting point of the new mathematical line are the coordinates of the first point of this InfiniteLine. The coordinates of the end point of the new mathematical line are the coordinates of the second point of this InfiniteLine.

The set property sets the coordinates of the first point of this InfiniteLine to the coordinates of the starting point of the specified mathematical line. It sets the coordinates of the second point of this InfiniteLine to the coordinates of the end point of the specified mathematical line.

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)

## Availability

DraftSight V1R1.4
