---
title: "IMultiply Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "IMultiply"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IMultiply.html"
---

# IMultiply Method (IMathTransform)

Multiplies two matrices together.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMultiply( _
   ByVal TransformObjIn As MathTransform _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim TransformObjIn As MathTransform
Dim value As MathTransform

value = instance.IMultiply(TransformObjIn)
```

### C#

```csharp
MathTransform IMultiply(
   MathTransform TransformObjIn
)
```

### C++/CLI

```cpp
MathTransform^ IMultiply(
   MathTransform^ TransformObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransformObjIn`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) by which to multiply the calling math transform

### Return Value

Newly created [math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object or null if the operation fails

## VBA Syntax

See [MathTransform::IMultiply](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~IMultiply.html).

## Remarks

The resulting transform is the result of transforming math transform with respect to the transformObjIn coordinate frame.

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[Multiply Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Multiply.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
