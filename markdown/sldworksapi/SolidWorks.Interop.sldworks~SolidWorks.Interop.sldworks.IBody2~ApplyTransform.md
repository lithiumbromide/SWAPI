---
title: "ApplyTransform Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ApplyTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.html"
---

# ApplyTransform Method (IBody2)

Applies a transform to this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyTransform( _
   ByVal Xform As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Xform As MathTransform
Dim value As System.Boolean

value = instance.ApplyTransform(Xform)
```

### C#

```csharp
System.bool ApplyTransform(
   MathTransform Xform
)
```

### C++/CLI

```cpp
System.bool ApplyTransform(
   MathTransform^ Xform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xform`: [Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) to apply

### Return Value

True if the transform is successfully applied, false if not

## VBA Syntax

See [Body2::ApplyTransform](ms-its:sldworksapivb6.chm::/sldworks~Body2~ApplyTransform.html).

## Examples

[Check Interference (VBA)](Check_Interference_using_Modeler_CheckInterference_Example_VB.htm)
[Combine Assembly Components into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)
[Cut Body in Half using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

By design, a temporary body is added to the part and displayed in the assembly. The origin of the temporary body is relative to the part instead of the assembly. As a work-around, insert an interim part in the assembly with the origin aligned with the assembly and add the temporary body to the interim part.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
