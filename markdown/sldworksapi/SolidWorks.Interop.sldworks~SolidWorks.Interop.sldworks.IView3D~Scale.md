---
title: "Scale Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Scale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Scale.html"
---

# Scale Property (IView3D)

Gets or sets this 3D View's scale.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.Double

instance.Scale = value

value = instance.Scale
```

### C#

```csharp
System.double Scale {get; set;}
```

### C++/CLI

```cpp
property System.double Scale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale of this 3D View

## VBA Syntax

See [View3D::Scale](ms-its:sldworksapivb6.chm::/sldworks~View3D~Scale.html).

## Examples

See the [IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html) examples.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
