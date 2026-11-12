---
title: "CausticsCast Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "CausticsCast"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~CausticsCast.html"
---

# CausticsCast Property (IRenderMaterial)

Gets or sets whether specular materials reflect caustic photons for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property CausticsCast As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.CausticsCast = value

value = instance.CausticsCast
```

### C#

```csharp
System.bool CausticsCast {get; set;}
```

### C++/CLI

```cpp
property System.bool CausticsCast {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if specular materials reflect caustic photons, false if not

## VBA Syntax

See [RenderMaterial::CausticsCast](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~CausticsCast.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
