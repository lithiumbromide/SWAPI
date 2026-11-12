---
title: "Multiply Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "Multiply"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Multiply.html"
---

# Multiply Method (IMathTransform)

Multiplies two matrices together.

## Syntax

### Visual Basic (Declaration)

```vb
Function Multiply( _
   ByVal TransformObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim TransformObjIn As System.Object
Dim value As System.Object

value = instance.Multiply(TransformObjIn)
```

### C#

```csharp
System.object Multiply(
   System.object TransformObjIn
)
```

### C++/CLI

```cpp
System.Object^ Multiply(
   System.Object^ TransformObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransformObjIn`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) by which to multiply the calling math transform

### Return Value

Newly created [math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object or null or Nothing if the operation fails

## VBA Syntax

See [MathTransform::Multiply](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~Multiply.html).

## Examples

[Set Components and Transforms for Interference Detection (C#)](Set_Components_and_Transforms_for_Interference_Detection_Example_CSharp.htm)
[Set Components and Transforms for Interference Detection (VB.NET)](Set_Components_and_Transforms_for_Interference_Detection_Example_VBNET.htm)
[Set Components and Transforms for Interference Detection (VBA)](Set_Components_and_Transforms_for_Interference_Detection_Example_VB.htm)

## Remarks

The resulting transform is the result of transforming the math transform with respect to the transformObjIn coordinate frame.

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::IMultiply Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IMultiply.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
