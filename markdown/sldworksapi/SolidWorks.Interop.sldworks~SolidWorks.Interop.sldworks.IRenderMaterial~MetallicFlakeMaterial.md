---
title: "MetallicFlakeMaterial Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MetallicFlakeMaterial"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicFlakeMaterial.html"
---

# MetallicFlakeMaterial Property (IRenderMaterial)

Gets or sets the metallic flake material for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property MetallicFlakeMaterial As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.MetallicFlakeMaterial = value

value = instance.MetallicFlakeMaterial
```

### C#

```csharp
System.int MetallicFlakeMaterial {get; set;}
```

### C++/CLI

```cpp
property System.int MetallicFlakeMaterial {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 0 = Aluminum

1 = Copper

2 = Gold

3 = Silver

## VBA Syntax

See [RenderMaterial::MetallicFlakeMaterial](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MetallicFlakeMaterial.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
