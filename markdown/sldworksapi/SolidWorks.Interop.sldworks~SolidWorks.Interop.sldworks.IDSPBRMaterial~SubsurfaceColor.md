---
title: "SubsurfaceColor Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "SubsurfaceColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SubsurfaceColor.html"
---

# SubsurfaceColor Property (IDSPBRMaterial)

Gets or sets the subsurface scattering color value for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property SubsurfaceColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.SubsurfaceColor = value

value = instance.SubsurfaceColor
```

### C#

```csharp
System.int SubsurfaceColor {get; set;}
```

### C++/CLI

```cpp
property System.int SubsurfaceColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Subsurface scattering color

## VBA Syntax

See [DSPBRMaterial::SubsurfaceColor](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~SubsurfaceColor.html).

## Remarks

This property returns a [COLORREF](https://learn.microsoft.com/en-us/windows/win32/gdi/colorref) that is represented as a decimal. The DSPBR tab in the user interface shows colors in RGB format. You can find online converters to convert RGB to hexadecimal or decimal.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Subsurface color" in the pop up. Click **Next result** repeatedly.

- Search for "Subsurface scattering color in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
