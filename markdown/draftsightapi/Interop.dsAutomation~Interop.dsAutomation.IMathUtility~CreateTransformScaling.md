---
title: "CreateTransformScaling Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateTransformScaling"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformScaling.html"
---

# CreateTransformScaling Method (IMathUtility)

Creates a mathematical transformation matrix that scales about the specified center point using the specified scaling factor.

## Syntax

### Visual Basic

```vb
Function CreateTransformScaling( _
   ByVal CenterPoint As MathPoint, _
   ByVal Scale As System.Double _
) As MathTransform
```

### C#

```csharp
MathTransform CreateTransformScaling(
   MathPoint CenterPoint,
   System.double Scale
)
```

### JScript

```
function CreateTransformScaling(
   CenterPoint : MathPoint,
   Scale : System.double
) : MathTransform;
```

### Managed Extensions for C++

```
MathTransform* CreateTransformScaling(
   MathPoint* CenterPoint,
   System.double Scale
)
```

### C++/CLI

```cpp
MathTransform^ CreateTransformScaling(
   MathPoint^ CenterPoint,
   System.double Scale
)
```

### Parameters

- `CenterPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `Scale`: Scaling factor

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
[IMathUtility::CreateTransformRotation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformRotation.html)
[IMathUtility::CreateTransformTranslation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformTranslation.html)

## Availability

DraftSight V1R1.4
