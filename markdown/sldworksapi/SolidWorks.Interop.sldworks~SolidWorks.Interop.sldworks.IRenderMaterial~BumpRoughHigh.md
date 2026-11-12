---
title: "BumpRoughHigh Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpRoughHigh"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpRoughHigh.html"
---

# BumpRoughHigh Property (IRenderMaterial)

Gets or sets the high threshold of the surface finish for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpRoughHigh As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpRoughHigh = value

value = instance.BumpRoughHigh
```

### C#

```csharp
System.double BumpRoughHigh {get; set;}
```

### C++/CLI

```cpp
property System.double BumpRoughHigh {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

High threshold

## VBA Syntax

See [RenderMaterial::BumpRoughHigh](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpRoughHigh.html).

## Remarks

The high threshold is an absolute distance from the neutral surface (amplitude = 0). The high threshold extends further away from the neutral surface than the low threshold.

For positive [amplitude](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~BumpAmplitude.html), the high threshold flattens the peaks of the surface finish. For negative amplitude, the high threshold flattens the valleys of the surface finish.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
