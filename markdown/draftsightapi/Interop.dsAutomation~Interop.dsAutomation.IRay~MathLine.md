---
title: "MathLine Property (IRay)"
project: ""
interface: "IRay"
member: "MathLine"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~MathLine.html"
---

# MathLine Property (IRay)

Gets the mathematical line that is derived from this Ray or sets the base and through points of this Ray using the specified mathematical line.

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

The get property returns a new mathematical line of type [dsMathLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsMathLineType_e.html).dsMathLineType_Ray. The coordinates of the starting point of the new mathematical line are the coordinates of the base point of this Ray. The coordinates of the end point of the new mathematical line are the coordinates of the through point of this Ray.

The set property sets the coordinates of the base point of this Ray to the coordinates of the starting point of the specified mathematical line. It sets the coordinates of the through point of this Ray to the coordinates of the end point of the specified mathematical line.

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)

## Availability

DraftSight V1R1.4
