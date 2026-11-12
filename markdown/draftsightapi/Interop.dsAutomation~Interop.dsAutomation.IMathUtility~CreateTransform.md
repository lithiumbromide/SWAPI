---
title: "CreateTransform Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateTransform"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransform.html"
---

# CreateTransform Method (IMathUtility)

Creates a mathematical transformation matrix using the specified data array.

## Syntax

### Visual Basic

```vb
Function CreateTransform( _
   ByVal DataDblArray As System.Object _
) As MathTransform
```

### C#

```csharp
MathTransform CreateTransform(
   System.object DataDblArray
)
```

### JScript

```
function CreateTransform(
   DataDblArray : System.Object
) : MathTransform;
```

### Managed Extensions for C++

```
MathTransform* CreateTransform(
   System.Object* DataDblArray
)
```

### C++/CLI

```cpp
MathTransform^ CreateTransform(
   System.Object^ DataDblArray
)
```

### Parameters

- `DataDblArray`: Array of 16 doubles of the elements of the transformation matrix

### Return Value

[IMathTransform](Interop.dsAutomation~Interop.dsAutomation.IMathTransform.html)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateTransformMirroringAboutLine Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutLine.html)
[IMathUtility::CreateTransformMirroringAboutPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPlane.html)
[IMathUtility::CreateTransformMirroringAboutPoint Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformMirroringAboutPoint.html)
[IMathUtility::CreateTransformProjection Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformProjection.html)
[IMathUtility::CreateTransformRotation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformRotation.html)
[IMathUtility::CreateTransformScaling Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformScaling.html)
[IMathUtility::CreateTransformTranslation Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateTransformTranslation.html)

## Availability

DraftSight V1R1.4
