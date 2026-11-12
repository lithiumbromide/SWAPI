---
title: "Albedo Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Albedo"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Albedo.html"
---

# Albedo Property (IDSPBRMaterial)

Gets or sets the ratio of reflected radiation to incident radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Albedo As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.Albedo = value

value = instance.Albedo
```

### C#

```csharp
System.int Albedo {get; set;}
```

### C++/CLI

```cpp
property System.int Albedo {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Albedo number

## VBA Syntax

See [DSPBRMaterial::Albedo](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Albedo.html).

## Remarks

This property returns a [COLORREF](https://learn.microsoft.com/en-us/windows/win32/gdi/colorref) that is represented as a decimal. The DSPBR tab in the user interface shows colors in RGB format. You can find online converters to convert RGB to hexadecimal or decimal.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Albedo" in the pop up. Click **Next result** repeatedly.

- Search for "Albedo" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
