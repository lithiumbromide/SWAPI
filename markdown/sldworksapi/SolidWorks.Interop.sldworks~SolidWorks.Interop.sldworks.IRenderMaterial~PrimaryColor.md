---
title: "PrimaryColor Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "PrimaryColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~PrimaryColor.html"
---

# PrimaryColor Property (IRenderMaterial)

Gets or sets the primary color of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrimaryColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.PrimaryColor = value

value = instance.PrimaryColor
```

### C#

```csharp
System.int PrimaryColor {get; set;}
```

### C++/CLI

```cpp
property System.int PrimaryColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value

## VBA Syntax

See [RenderMaterial::PrimaryColor](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~PrimaryColor.html).

## Remarks

This property corresponds to the Current Color 1 control on the Color/Image tab of the Appearances PropertyManager page.

To get or set:

- Current Color 2, call [IRenderMaterial::SecondaryColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SecondaryColor.html).
- Current Color 3, call [IRenderMaterial::TertiaryColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~TertiaryColor.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
