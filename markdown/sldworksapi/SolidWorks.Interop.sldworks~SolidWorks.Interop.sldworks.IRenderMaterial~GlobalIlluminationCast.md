---
title: "GlobalIlluminationCast Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GlobalIlluminationCast"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GlobalIlluminationCast.html"
---

# GlobalIlluminationCast Property (IRenderMaterial)

Gets whether specular materials reflect photons for illuminating this appearance..

## Syntax

### Visual Basic (Declaration)

```vb
Property GlobalIlluminationCast As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.GlobalIlluminationCast = value

value = instance.GlobalIlluminationCast
```

### C#

```csharp
System.bool GlobalIlluminationCast {get; set;}
```

### C++/CLI

```cpp
property System.bool GlobalIlluminationCast {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if specular materials reflect photons, false if not

## VBA Syntax

See [RenderMaterial::GlobalIlluminationCast](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GlobalIlluminationCast.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
