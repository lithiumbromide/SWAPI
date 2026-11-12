---
title: "CreateTransformProjection Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateTransformProjection"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformProjection.html"
---

# CreateTransformProjection Method (IMathUtility)

Creates a mathematical transformation matrix that projects onto the specified plane in the specified direction.

## Syntax

### Visual Basic

```vb
Function CreateTransformProjection( _
   ByVal ProjectionPlane As MathPlane, _
   ByVal ProjectionDirection As MathVector _
) As MathTransform
```

### C#

```csharp
MathTransform CreateTransformProjection(
   MathPlane ProjectionPlane,
   MathVector ProjectionDirection
)
```

### JScript

```
function CreateTransformProjection(
   ProjectionPlane : MathPlane,
   ProjectionDirection : MathVector
) : MathTransform;
```

### Managed Extensions for C++

```
MathTransform* CreateTransformProjection(
   MathPlane* ProjectionPlane,
   MathVector* ProjectionDirection
)
```

### C++/CLI

```cpp
MathTransform^ CreateTransformProjection(
   MathPlane^ ProjectionPlane,
   MathVector^ ProjectionDirection
)
```

### Parameters

- `ProjectionPlane`: [IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
- `ProjectionDirection`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)

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
[IMathUtility::CreateTransformRotation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformRotation.html)
[IMathUtility::CreateTransformScaling Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformScaling.html)
[IMathUtility::CreateTransformTranslation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformTranslation.html)

## Availability

DraftSight V1R1.4
