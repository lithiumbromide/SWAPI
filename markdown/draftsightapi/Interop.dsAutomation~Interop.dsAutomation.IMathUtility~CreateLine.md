---
title: "CreateLine Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateLine.html"
---

# CreateLine Method (IMathUtility)

Creates a mathematical line of the specified type passing through the specified points.

## Syntax

### Visual Basic

```vb
Function CreateLine( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double, _
   ByVal Type As dsMathLineType_e _
) As MathLine
```

### C#

```csharp
MathLine CreateLine(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ,
   dsMathLineType_e Type
)
```

### JScript

```
function CreateLine(
   StartX : System.double,
   StartY : System.double,
   StartZ : System.double,
   EndX : System.double,
   EndY : System.double,
   EndZ : System.double,
   Type : dsMathLineType_e
) : MathLine;
```

### Managed Extensions for C++

```
MathLine* CreateLine(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ,
   dsMathLineType_e Type
)
```

### C++/CLI

```cpp
MathLine^ CreateLine(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ,
   dsMathLineType_e Type
)
```

### Parameters

- `StartX`: x coordinate of starting point
- `StartY`: y coordinate of starting point
- `StartZ`: z coordinate of starting point
- `EndX`: x coordinate of ending point
- `EndY`: y coordinate of ending point
- `EndZ`: z coordinate of ending point
- `Type`: Type of line as defined in [dsMathLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsMathLineType_e.html)

### Return Value

[IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)

## Examples

[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateLineByPointAndDirection Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateLineByPointAndDirection.html)

## Availability

DraftSight V1R1.4
