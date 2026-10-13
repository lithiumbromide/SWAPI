---
title: "Reflectivity Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Reflectivity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Reflectivity.html"
---

# Reflectivity Property (IRenderMaterial)

Gets or sets the reflectivity for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reflectivity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Reflectivity = value

value = instance.Reflectivity
```

### C#

```csharp
System.double Reflectivity {get; set;}
```

### C++/CLI

```cpp
property System.double Reflectivity {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reflectivity

## VBA Syntax

See[RenderMaterial::Reflectivity](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Reflectivity.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
