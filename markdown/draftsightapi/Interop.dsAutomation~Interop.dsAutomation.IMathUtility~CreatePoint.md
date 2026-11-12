---
title: "CreatePoint Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreatePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreatePoint.html"
---

# CreatePoint Method (IMathUtility)

Creates a mathematical point using the specified coordinates.

## Syntax

### Visual Basic

```vb
Function CreatePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As MathPoint
```

### C#

```csharp
MathPoint CreatePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function CreatePoint(
   X : System.double,
   Y : System.double,
   Z : System.double
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* CreatePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
MathPoint^ CreatePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

### Return Value

[IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

## Examples

[Get Distance Between Two Math Points (VB.NET)](Get_Distance_Between_Two_Math_Points_Example_VBNET.htm)
[Get Distance Between Two Math Points (C#)](Get_Distance_Between_Two_Math_Points_Example_CSharp.htm)
[Get Distance Between Two Math Points (JavaScript)](Get_Distance_Between_Two_Math_Points_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)
[Get Distance Between Two Math Points (VBA)](Get_Distance_Between_Two_Math_Points_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)

## Availability

DraftSight V1R1.4
