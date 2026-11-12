---
title: "IMultiplyTransform Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "IMultiplyTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IMultiplyTransform.html"
---

# IMultiplyTransform Method (IMathPoint)

Multiplies a math point with a math transform; the point is rotated, scaled, and then translated.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMultiplyTransform( _
   ByVal TransformObjIn As MathTransform _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim TransformObjIn As MathTransform
Dim value As MathPoint

value = instance.IMultiplyTransform(TransformObjIn)
```

### C#

```csharp
MathPoint IMultiplyTransform(
   MathTransform TransformObjIn
)
```

### C++/CLI

```cpp
MathPoint^ IMultiplyTransform(
   MathTransform^ TransformObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransformObjIn`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) by which to multiply this math point

### Return Value

Newly created translated [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or null if the operation fails

## VBA Syntax

See [MathPoint::IMultiplyTransform](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~IMultiplyTransform.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::MultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~MultiplyTransform.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
