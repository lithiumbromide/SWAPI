---
title: "TertiaryColor Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "TertiaryColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~TertiaryColor.html"
---

# TertiaryColor Property (IRenderMaterial)

Gets or sets the tertiary color of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property TertiaryColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.TertiaryColor = value

value = instance.TertiaryColor
```

### C#

```csharp
System.int TertiaryColor {get; set;}
```

### C++/CLI

```cpp
property System.int TertiaryColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value

## VBA Syntax

See [RenderMaterial::TertiaryColor](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~TertiaryColor.html).

## Remarks

This property corresponds to the Current Color 3 control on the Color/Image tab of the Appearances PropertyManager page.

To get or set:

- Current Color 1, call [IRenderMaterial::PrimaryColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~PrimaryColor.html).
- Current Color 2, call [IRenderMaterial::SecondaryColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SecondaryColor.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
