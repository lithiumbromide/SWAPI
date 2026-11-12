---
title: "FlipFlop Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "FlipFlop"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlipFlop.html"
---

# FlipFlop Property (IDSPBRMaterial)

Gets or sets the directional-dependent color (flip flop) effects of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipFlop As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.FlipFlop = value

value = instance.FlipFlop
```

### C#

```csharp
System.double FlipFlop {get; set;}
```

### C++/CLI

```cpp
property System.double FlipFlop {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (none) default <= Flip flop value <= 1.0 (full)

## VBA Syntax

See [DSPBRMaterial::FlipFlop](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~FlipFlop.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Flip-flop" in the pop up. Click **Next result** repeatedly.

- Search for "Flipflop in materials science and engineering" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
