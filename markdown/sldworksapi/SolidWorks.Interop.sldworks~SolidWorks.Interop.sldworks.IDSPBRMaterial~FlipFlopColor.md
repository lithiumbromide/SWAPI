---
title: "FlipFlopColor Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "FlipFlopColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlipFlopColor.html"
---

# FlipFlopColor Property (IDSPBRMaterial)

Gets or sets the flake color at normal incidence if flip flop effect is enabled for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipFlopColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.FlipFlopColor = value

value = instance.FlipFlopColor
```

### C#

```csharp
System.int FlipFlopColor {get; set;}
```

### C++/CLI

```cpp
property System.int FlipFlopColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flip flop color

## VBA Syntax

See [DSPBRMaterial::FlipFlopColor](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~FlipFlopColor.html).

## Remarks

This property:

- is valid only if [IDSPBRMaterial::FlipFlop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlipFlop.html) is enabled.

- returns a [COLORREF](https://learn.microsoft.com/en-us/windows/win32/gdi/colorref) that is represented as a decimal. The DSPBR tab in the user interface shows colors in RGB format. You can find online converters to convert RGB to hexadecimal or decimal.Search for "Flipflop color in materials science and engineering" in your browser to obtain more information about this property.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Flake color at normal incidence" in the pop up. Click **Next result** repeatedly.

- Search for "Flipflop in materials science and engineering" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
