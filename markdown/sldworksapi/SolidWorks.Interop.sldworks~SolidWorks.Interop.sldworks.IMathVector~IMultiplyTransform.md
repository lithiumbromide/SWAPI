---
title: "IMultiplyTransform Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "IMultiplyTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IMultiplyTransform.html"
---

# IMultiplyTransform Method (IMathVector)

Multiplies this math vector by the specified math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMultiplyTransform( _
   ByVal TransformObjIn As MathTransform _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim TransformObjIn As MathTransform
Dim value As MathVector

value = instance.IMultiplyTransform(TransformObjIn)
```

### C#

```csharp
MathVector IMultiplyTransform(
   MathTransform TransformObjIn
)
```

### C++/CLI

```cpp
MathVector^ IMultiplyTransform(
   MathTransform^ TransformObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransformObjIn`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) by which to multiply the math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathVector::IMultiplyTransform](ms-its:sldworksapivb6.chm::/sldworks~MathVector~IMultiplyTransform.html).

## Remarks

The matrix is rotated and then scaled. It is not transformed because the math vector is assumed to be positionless.

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::MultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~MultiplyTransform.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
