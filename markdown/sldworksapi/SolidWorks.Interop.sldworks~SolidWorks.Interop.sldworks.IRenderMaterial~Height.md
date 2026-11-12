---
title: "Height Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Height.html"
---

# Height Property (IRenderMaterial)

Gets or sets the height for mapping this appearance texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.double Height {get; set;}
```

### C++/CLI

```cpp
property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height

## VBA Syntax

See [RenderMaterial::Height](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Height.html).

## Examples

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)
[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)
[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

## Remarks

Call [IRenderMaterial::Width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Width.html) to set the width of the appearance texture. If [IRenderMaterial::FixedAspectRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FixedAspectRatio.html) is true, then the image is uniformly scaled when either the width or height is changed.

To have the height and width of the appearance texture automatically stretch to fit a selected entity, call [IRenderMaterial::FitHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FitHeight.html) and [IRenderMaterial::FitWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FitWidth.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
