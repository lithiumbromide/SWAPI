---
title: "MetallicRoughness Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MetallicRoughness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicRoughness.html"
---

# MetallicRoughness Property (IRenderMaterial)

Gets or sets the size (coarseness) any highlights on the surface for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property MetallicRoughness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.MetallicRoughness = value

value = instance.MetallicRoughness
```

### C#

```csharp
System.double MetallicRoughness {get; set;}
```

### C++/CLI

```cpp
property System.double MetallicRoughness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Size of any highlights on the surface

## VBA Syntax

See [RenderMaterial::MetallicRoughness](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MetallicRoughness.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
