---
title: "BumpUseMappingScale Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpUseMappingScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpUseMappingScale.html"
---

# BumpUseMappingScale Property (IRenderMaterial)

Gets or sets whether to use the material's scale and mapping for the surface finish of this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpUseMappingScale As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.BumpUseMappingScale = value

value = instance.BumpUseMappingScale
```

### C#

```csharp
System.bool BumpUseMappingScale {get; set;}
```

### C++/CLI

```cpp
property System.bool BumpUseMappingScale {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the material's scale and mapping, false to not

## VBA Syntax

See [RenderMaterial::BumpUseMappingScale](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpUseMappingScale.html).

## Remarks

If BumpUseMappingScale is set to FALSE, then specify the [scale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~BumpScale.html) and mapping for this surface finish for this appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
