---
title: "SpecularTintColor Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "SpecularTintColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SpecularTintColor.html"
---

# SpecularTintColor Property (IDSPBRMaterial)

Gets or sets the specular tint to adjust the color of the specular lobe near theta = zero degrees for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecularTintColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.SpecularTintColor = value

value = instance.SpecularTintColor
```

### C#

```csharp
System.int SpecularTintColor {get; set;}
```

### C++/CLI

```cpp
property System.int SpecularTintColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Specular tint

## VBA Syntax

See [DSPBRMaterial::SpecularTintColor](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~SpecularTintColor.html).

## Remarks

This property returns a [COLORREF](https://learn.microsoft.com/en-us/windows/win32/gdi/colorref) that is represented as a decimal. The DSPBR tab in the user interface shows colors in RGB format. You can find online converters to convert RGB to hexadecimal or decimal.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Specular tint" in the pop up. Click **Next result** repeatedly.

- Search for "Specular tint color in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
