---
title: "IInverse Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "IInverse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IInverse.html"
---

# IInverse Method (IMathTransform)

Creates a new math transform by inverting the values in an already existing math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInverse() As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim value As MathTransform

value = instance.IInverse()
```

### C#

```csharp
MathTransform IInverse()
```

### C++/CLI

```cpp
MathTransform^ IInverse();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) or NULL if the operation fails

## VBA Syntax

See [MathTransform::IInverse](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~IInverse.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::Inverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Inverse.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
