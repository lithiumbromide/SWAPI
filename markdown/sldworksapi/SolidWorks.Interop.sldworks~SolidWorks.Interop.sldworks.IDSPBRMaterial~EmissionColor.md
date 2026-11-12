---
title: "EmissionColor Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "EmissionColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionColor.html"
---

# EmissionColor Property (IDSPBRMaterial)

Gets or sets the emission color of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property EmissionColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.EmissionColor = value

value = instance.EmissionColor
```

### C#

```csharp
System.int EmissionColor {get; set;}
```

### C++/CLI

```cpp
property System.int EmissionColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Emission color

## VBA Syntax

See [DSPBRMaterial::EmissionColor](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~EmissionColor.html).

## Remarks

This property returns a [COLORREF](https://learn.microsoft.com/en-us/windows/win32/gdi/colorref) that is represented as a decimal. The DSPBR tab in the user interface shows colors in RGB format. You can find online converters to convert RGB to hexadecimal or decimal.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Emission color" in the pop up. Click **Next result** repeatedly.

- Search for "emission color" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
