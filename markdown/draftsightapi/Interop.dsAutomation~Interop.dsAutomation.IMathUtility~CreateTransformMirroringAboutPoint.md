---
title: "CreateTransformMirroringAboutPoint Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateTransformMirroringAboutPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPoint.html"
---

# CreateTransformMirroringAboutPoint Method (IMathUtility)

Creates a mathematical transformation matrix that mirrors about the specified point.

## Syntax

### Visual Basic

```vb
Function CreateTransformMirroringAboutPoint( _
   ByVal MirrorPoint As MathPoint _
) As MathTransform
```

### C#

```csharp
MathTransform CreateTransformMirroringAboutPoint(
   MathPoint MirrorPoint
)
```

### JScript

```
function CreateTransformMirroringAboutPoint(
   MirrorPoint : MathPoint
) : MathTransform;
```

### Managed Extensions for C++

```
MathTransform* CreateTransformMirroringAboutPoint(
   MathPoint* MirrorPoint
)
```

### C++/CLI

```cpp
MathTransform^ CreateTransformMirroringAboutPoint(
   MathPoint^ MirrorPoint
)
```

### Parameters

- `MirrorPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

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
[IMathUtility::CreateTransformProjection Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformProjection.html)
[IMathUtility::CreateTransformRotation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformRotation.html)
[IMathUtility::CreateTransformScaling Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformScaling.html)
[IMathUtility::CreateTransformTranslation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformTranslation.html)

## Availability

DraftSight V1R1.4
