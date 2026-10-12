---
title: "Rotation Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Rotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Rotation.html"
---

# Rotation Property (IView3D)

Gets or sets the 3D View rotation with respect to the Front view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Rotation As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As MathTransform

instance.Rotation = value

value = instance.Rotation
```

### C#

```csharp
MathTransform Rotation {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ Rotation {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [View3D::Rotation](ms-its:sldworksapivb6.chm::/sldworks~View3D~Rotation.html).

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
