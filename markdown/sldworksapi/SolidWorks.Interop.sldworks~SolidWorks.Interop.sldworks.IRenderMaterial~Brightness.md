---
title: "Brightness Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Brightness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Brightness.html"
---

# Brightness Property (IRenderMaterial)

Gets or sets how emissive the material is for the Constant illumination type for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Brightness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Brightness = value

value = instance.Brightness
```

### C#

```csharp
System.double Brightness {get; set;}
```

### C++/CLI

```cpp
property System.double Brightness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Brightness

## VBA Syntax

See [RenderMaterial::Brightness](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Brightness.html).

## Remarks

This property corresponds to the Brightness control on the Illumination tab of the Appearances PropertyManager page when Illumination is Constant.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
