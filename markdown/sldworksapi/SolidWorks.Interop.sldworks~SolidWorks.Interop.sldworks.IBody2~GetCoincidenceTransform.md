---
title: "GetCoincidenceTransform Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetCoincidenceTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform.html"
---

# GetCoincidenceTransform Method (IBody2)

Obsolete. Superseded by [IBody2::GetCoincidenceTransform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetCoincidenceTransform2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoincidenceTransform( _
   ByVal BodyDispIn As System.Object, _
   ByRef Xform As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim BodyDispIn As System.Object
Dim Xform As MathTransform
Dim value As System.Boolean

value = instance.GetCoincidenceTransform(BodyDispIn, Xform)
```

### C#

```csharp
System.bool GetCoincidenceTransform(
   System.object BodyDispIn,
   out MathTransform Xform
)
```

### C++/CLI

```cpp
System.bool GetCoincidenceTransform(
   System.Object^ BodyDispIn,
   [Out] MathTransform^ Xform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyDispIn`: Input body
- `Xform`: Pointer to the [transformation matrix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

### Return Value

True if the bodies (the body on which the method is invoked and the input body) can coincide by applying appropriate transforms, false if not

## VBA Syntax

See [Body2::GetCoincidenceTransform](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetCoincidenceTransform.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
