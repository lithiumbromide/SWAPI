---
title: "MathLine Property (ILine)"
project: ""
interface: "ILine"
member: "MathLine"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~MathLine.html"
---

# MathLine Property (ILine)

Gets a mathematical line that is derived from this Line or sets the first and second points of this Line using the specified mathematical line.

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

## Examples

[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)

## Remarks

The get property returns a new mathematical line of type [dsMathLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsMathLineType_e.html).dsMathLineType_Bounded. The coordinates of the starting point of the new mathematical line are the coordinates of the first point of this Line. The coordinates of the end point of the new mathematical line are the coordinates of the second point of this Line.

The set property sets the coordinates of the first point of this Line to the coordinates of the starting point of the specified mathematical line. It sets the coordinates of the second point of this Line to the coordinates of the end point of the specified mathematical line.

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)

## Availability

DraftSight V1R1.4
