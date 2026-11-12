---
title: "UseJacobianCheckForShells2 Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "UseJacobianCheckForShells2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells2.html"
---

# UseJacobianCheckForShells2 Property (ICWMesh)

Gets or sets whether to perform a Jacobian check for shells.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseJacobianCheckForShells2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Boolean

instance.UseJacobianCheckForShells2 = value

value = instance.UseJacobianCheckForShells2
```

### C#

```csharp
System.bool UseJacobianCheckForShells2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseJacobianCheckForShells2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to perform the Jacobian check, 0 or false to not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
