---
title: "CreateTransformRotation Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateTransformRotation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformRotation.html"
---

# CreateTransformRotation Method (IMathUtility)

Creates a mathematical transformation matrix that represents the rotation by the specified angle about the specified axis vector whose center is the specified point.

## Syntax

### Visual Basic

```vb
Function CreateTransformRotation( _
   ByVal CenterPoint As MathPoint, _
   ByVal Axis As MathVector, _
   ByVal Angle As System.Double _
) As MathTransform
```

### C#

```csharp
MathTransform CreateTransformRotation(
   MathPoint CenterPoint,
   MathVector Axis,
   System.double Angle
)
```

### JScript

```
function CreateTransformRotation(
   CenterPoint : MathPoint,
   Axis : MathVector,
   Angle : System.double
) : MathTransform;
```

### Managed Extensions for C++

```
MathTransform* CreateTransformRotation(
   MathPoint* CenterPoint,
   MathVector* Axis,
   System.double Angle
)
```

### C++/CLI

```cpp
MathTransform^ CreateTransformRotation(
   MathPoint^ CenterPoint,
   MathVector^ Axis,
   System.double Angle
)
```

### Parameters

- `CenterPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html); center point of Axis
- `Axis`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `Angle`: Angle in radians of rotation about Axis

### Return Value

[IMathTransform](Interop.dsAutomation~Interop.dsAutomation.IMathTransform.html)

## Examples

[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateTransform Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransform.html)
[IMathUtility::CreateTransformMirroringAboutLine Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutLine.html)
[IMathUtility::CreateTransformMirroringAboutPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPlane.html)
[IMathUtility::CreateTransformMirroringAboutPoint Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPoint.html)
[IMathUtility::CreateTransformProjection Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformProjection.html)
[IMathUtility::CreateTransformScaling Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformScaling.html)
[IMathUtility::CreateTransformTranslation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformTranslation.html)

## Availability

DraftSight V1R1.4
