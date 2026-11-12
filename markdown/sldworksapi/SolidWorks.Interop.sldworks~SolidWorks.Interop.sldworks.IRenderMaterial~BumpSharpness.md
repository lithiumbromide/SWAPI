---
title: "BumpSharpness Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpSharpness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpSharpness.html"
---

# BumpSharpness Property (IRenderMaterial)

Gets or sets the sharpness, which influences the shape of the surface finish, of this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpSharpness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpSharpness = value

value = instance.BumpSharpness
```

### C#

```csharp
System.double BumpSharpness {get; set;}
```

### C++/CLI

```cpp
property System.double BumpSharpness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sharpness

## VBA Syntax

See [RenderMaterial::BumpSharpness](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpSharpness.html).

## Remarks

A higher sharpness value retains the original shape of the surface finish; a lower sharpness value filters (smoothens) the surface-finish details.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
