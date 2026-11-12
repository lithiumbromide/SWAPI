---
title: "GetCoincidenceTransform2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetCoincidenceTransform2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform2.html"
---

# GetCoincidenceTransform2 Method (IBody2)

Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoincidenceTransform2( _
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

value = instance.GetCoincidenceTransform2(BodyDispIn, Xform)
```

### C#

```csharp
System.bool GetCoincidenceTransform2(
   System.object BodyDispIn,
   out MathTransform Xform
)
```

### C++/CLI

```cpp
System.bool GetCoincidenceTransform2(
   System.Object^ BodyDispIn,
   [Out] MathTransform^ Xform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyDispIn`: [Input body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `Xform`: Pointer to the [transformation matrix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

### Return Value

True if this body and the input body can coincide by applying the transformation matrix, false if not

## VBA Syntax

See [Body2::GetCoincidenceTransform2](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetCoincidenceTransform2.html).

## Examples

[Calculate Transformations in Part (C#)](Calculate_Transformations_in_Part_Example_CSharp.htm)
[Calculate Transformations in Part (VB.NET)](Calculate_Transformations_in_Part_Example_VBNET.htm)
[Calculate Transformations in Part (VBA)](Calculate_Transformations_in_Part_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2013 SP1, Revision Number 21.1
