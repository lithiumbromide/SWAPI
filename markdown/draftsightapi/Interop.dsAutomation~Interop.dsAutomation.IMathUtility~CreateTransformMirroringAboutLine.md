---
title: "CreateTransformMirroringAboutLine Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateTransformMirroringAboutLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutLine.html"
---

# CreateTransformMirroringAboutLine Method (IMathUtility)

Creates a mathematical transformation matrix that mirrors about the specified line.

## Syntax

### Visual Basic

```vb
Function CreateTransformMirroringAboutLine( _
   ByVal MirrorLine As MathLine _
) As MathTransform
```

### C#

```csharp
MathTransform CreateTransformMirroringAboutLine(
   MathLine MirrorLine
)
```

### JScript

```
function CreateTransformMirroringAboutLine(
   MirrorLine : MathLine
) : MathTransform;
```

### Managed Extensions for C++

```
MathTransform* CreateTransformMirroringAboutLine(
   MathLine* MirrorLine
)
```

### C++/CLI

```cpp
MathTransform^ CreateTransformMirroringAboutLine(
   MathLine^ MirrorLine
)
```

### Parameters

- `MirrorLine`: [IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)

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
[IMathUtility::CreateTransformMirroringAboutPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPlane.html)
[IMathUtility::CreateTransformMirroringAboutPoint Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPoint.html)
[IMathUtility::CreateTransformProjection Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformProjection.html)
[IMathUtility::CreateTransformRotation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformRotation.html)
[IMathUtility::CreateTransformScaling Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformScaling.html)

## Availability

DraftSight V1R1.4
