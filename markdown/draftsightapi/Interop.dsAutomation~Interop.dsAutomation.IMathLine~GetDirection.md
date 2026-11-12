---
title: "GetDirection Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "GetDirection"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetDirection.html"
---

# GetDirection Method (IMathLine)

Gets a unit vector that is parallel to this mathematical line, pointing in a positive direction.

## Syntax

### Visual Basic

```vb
Sub GetDirection( _
   ByRef Vector As MathVector _
)
```

### C#

```csharp
void GetDirection(
   out MathVector Vector
)
```

### JScript

```
function GetDirection(
   Vector : MathVector
);
```

### Managed Extensions for C++

```
void GetDirection(
   [PARAMFLAG::Out] MathVector* Vector
)
```

### C++/CLI

```cpp
void GetDirection(
   [Out] MathVector^ Vector
)
```

### Parameters

- `Vector`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)

## Examples

[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)

## Availability

DraftSight V1R1.4
