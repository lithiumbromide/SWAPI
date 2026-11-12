---
title: "GetPosition Method (IMathPoint)"
project: ""
interface: "IMathPoint"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPoint~GetPosition.html"
---

# GetPosition Method (IMathPoint)

Gets the x, y, and z coordinates of this mathematical point.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPosition(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPosition(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## Examples

[Get Distance Between Two Math Points (C#)](Get_Distance_Between_Two_Math_Points_Example_CSharp.htm)
[Get Distance Between Two Math Points (VB.NET)](Get_Distance_Between_Two_Math_Points_Example_VBNET.htm)
[Get Distance Between Two Math Points (JavaScript)](Get_Distance_Between_Two_Math_Points_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)
[Get Distance Between Two Math Points (VBA)](Get_Distance_Between_Two_Math_Points_Example_VBA.htm)

## See Also

[IMathPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
[IMathPoint Members](Interop.dsAutomation~Interop.dsAutomation.IMathPoint_members.html)
[IMathPoint::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IMathPoint~SetPosition.html)

## Availability

DraftSight V1R1.4
