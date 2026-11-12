---
title: "CreateVector Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateVector"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateVector.html"
---

# CreateVector Method (IMathUtility)

Creates a unit vector with the specified coordinates.

## Syntax

### Visual Basic

```vb
Function CreateVector( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As MathVector
```

### C#

```csharp
MathVector CreateVector(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function CreateVector(
   X : System.double,
   Y : System.double,
   Z : System.double
) : MathVector;
```

### Managed Extensions for C++

```
MathVector* CreateVector(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
MathVector^ CreateVector(
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

[IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)

## Examples

[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)

## Availability

DraftSight V1R1.4
