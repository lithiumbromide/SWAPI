---
title: "CausticsReceive Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "CausticsReceive"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~CausticsReceive.html"
---

# CausticsReceive Property (IRenderMaterial)

Gets or sets whether diffuse materials absorb caustic photons for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property CausticsReceive As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.CausticsReceive = value

value = instance.CausticsReceive
```

### C#

```csharp
System.bool CausticsReceive {get; set;}
```

### C++/CLI

```cpp
property System.bool CausticsReceive {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if diffuse materials absorb caustic photons, false if not

## VBA Syntax

See [RenderMaterial::CausticsReceive](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~CausticsReceive.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
