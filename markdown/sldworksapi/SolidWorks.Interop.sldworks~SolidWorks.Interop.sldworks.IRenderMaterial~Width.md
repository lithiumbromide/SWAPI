---
title: "Width Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Width.html"
---

# Width Property (IRenderMaterial)

Gets or sets the width for mapping this appearance texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.double Width {get; set;}
```

### C++/CLI

```cpp
property System.double Width {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width

## VBA Syntax

See [RenderMaterial::Width](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Width.html).

## Examples

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)
[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)
[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

## Remarks

Call [IRenderMaterial::Height](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Height.html) to set the height of the appearance texture. If [IRenderMaterial::FixedAspectRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FixedAspectRatio.html) is true, then the image is uniformly scaled when either the width or height is changed.

To have the height and width of the appearance texture automatically stretch to fit a selected entity, call [IRenderMaterial::FitHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FitHeight.html) and [IRenderMaterial::FitWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FitWidth.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
