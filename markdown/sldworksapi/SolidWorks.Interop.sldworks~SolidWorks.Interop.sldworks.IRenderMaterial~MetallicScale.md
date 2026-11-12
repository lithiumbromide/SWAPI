---
title: "MetallicScale Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MetallicScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicScale.html"
---

# MetallicScale Property (IRenderMaterial)

Gets or sets the size of the metallic flakes in the metallic layer for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property MetallicScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.MetallicScale = value

value = instance.MetallicScale
```

### C#

```csharp
System.double MetallicScale {get; set;}
```

### C++/CLI

```cpp
property System.double MetallicScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Size of the metallic flakes in the metallic layer

## VBA Syntax

See [RenderMaterial::MetallicScale](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MetallicScale.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
