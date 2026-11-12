---
title: "Transform Property (IRefPlane)"
project: "SOLIDWORKS API Help"
interface: "IRefPlane"
member: "Transform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~Transform.html"
---

# Transform Property (IRefPlane)

Gets the plane transform with respect to the world.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Transform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlane
Dim value As MathTransform

value = instance.Transform
```

### C#

```csharp
MathTransform Transform {get;}
```

### C++/CLI

```cpp
property MathTransform^ Transform {
   MathTransform^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [RefPlane::Transform](ms-its:sldworksapivb6.chm::/sldworks~RefPlane~Transform.html).

## Examples

[Get the Normal and Origin of a Reference Plane Using Its Transform (VBA)](Get_the_Normal_and_Origin_of_a_Reference_Plane_Using_Its_Transform_Example_VB.htm)
[Get Transform of Plane (VBA)](Get_Transform_of_Plane_Example_VB.htm)

## See Also

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
