---
title: "NegativeJacobianRatioCheck2 Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "NegativeJacobianRatioCheck2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NegativeJacobianRatioCheck2.html"
---

# NegativeJacobianRatioCheck2 Property (ICWMesh)

Gets or sets whether to check for a negative Jacobian ratio while meshing.

## Syntax

### Visual Basic (Declaration)

```vb
Property NegativeJacobianRatioCheck2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Boolean

instance.NegativeJacobianRatioCheck2 = value

value = instance.NegativeJacobianRatioCheck2
```

### C#

```csharp
System.bool NegativeJacobianRatioCheck2 {get; set;}
```

### C++/CLI

```cpp
property System.bool NegativeJacobianRatioCheck2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to check for a negative Jacobian ratio, 0 or false to not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

For more information, read the **Jacobian Points** section of the **Simulation > Meshing >** **Mesh Quality Checks** topic in the SOLIDWORKS help.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
