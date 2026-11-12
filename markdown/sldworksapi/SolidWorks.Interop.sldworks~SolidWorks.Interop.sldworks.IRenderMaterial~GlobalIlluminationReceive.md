---
title: "GlobalIlluminationReceive Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GlobalIlluminationReceive"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GlobalIlluminationReceive.html"
---

# GlobalIlluminationReceive Property (IRenderMaterial)

Gets or sets whether diffuse materials absorb photons for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property GlobalIlluminationReceive As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.GlobalIlluminationReceive = value

value = instance.GlobalIlluminationReceive
```

### C#

```csharp
System.bool GlobalIlluminationReceive {get; set;}
```

### C++/CLI

```cpp
property System.bool GlobalIlluminationReceive {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if diffuse materials absorb photons, false if not

## VBA Syntax

See [RenderMaterial::GlobalIlluminationReceive](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GlobalIlluminationReceive.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
