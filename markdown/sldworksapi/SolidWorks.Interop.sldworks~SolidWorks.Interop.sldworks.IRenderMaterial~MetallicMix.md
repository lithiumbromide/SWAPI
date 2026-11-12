---
title: "MetallicMix Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MetallicMix"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicMix.html"
---

# MetallicMix Property (IRenderMaterial)

Gets or sets the metallic quality of a material for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property MetallicMix As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.MetallicMix = value

value = instance.MetallicMix
```

### C#

```csharp
System.double MetallicMix {get; set;}
```

### C++/CLI

```cpp
property System.double MetallicMix {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Metallic quality

## VBA Syntax

See [RenderMaterial::MetallicMix](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MetallicMix.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
