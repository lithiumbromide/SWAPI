---
title: "FixedAspectRatio Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "FixedAspectRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FixedAspectRatio.html"
---

# FixedAspectRatio Property (IRenderMaterial)

Gets or sets whether the aspect ratio is fixed for mapping this appearance texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedAspectRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.FixedAspectRatio = value

value = instance.FixedAspectRatio
```

### C#

```csharp
System.bool FixedAspectRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool FixedAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the aspect ratio is fixed, false if not

## VBA Syntax

See [RenderMaterial::FixedAspectRatio](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~FixedAspectRatio.html).

## Examples

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)
[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)
[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

## Remarks

When FixedAspect is true, then the image is uniformly scaled when either the [height](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Height.html) or [width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Width.html) is changed.

Use this property when changing the height or width of an appearance texture and wanting it uniformly scaled.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
