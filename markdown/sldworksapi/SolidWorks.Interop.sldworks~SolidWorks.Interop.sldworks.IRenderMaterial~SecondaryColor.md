---
title: "SecondaryColor Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SecondaryColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SecondaryColor.html"
---

# SecondaryColor Property (IRenderMaterial)

Gets or sets the secondary color of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondaryColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.SecondaryColor = value

value = instance.SecondaryColor
```

### C#

```csharp
System.int SecondaryColor {get; set;}
```

### C++/CLI

```cpp
property System.int SecondaryColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value

## VBA Syntax

See [RenderMaterial::SecondaryColor](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SecondaryColor.html).

## Remarks

This property corresponds to the Current Color 2 control on the Color/Image tab of the Appearances PropertyManager page.

To get or set:

- Current Color 1, call [IRenderMaterial::PrimaryColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~PrimaryColor.html).
- Current Color 3, call [IRenderMaterial::TertiaryColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~TertiaryColor.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
