---
title: "BumpTextureFilename Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpTextureFilename"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpTextureFilename.html"
---

# BumpTextureFilename Property (IRenderMaterial)

Obsolete. Superseded by IRenderMaterial::SurfaceFinishFile. Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpTextureFilename As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.String

instance.BumpTextureFilename = value

value = instance.BumpTextureFilename
```

### C#

```csharp
System.string BumpTextureFilename {get; set;}
```

### C++/CLI

```cpp
property System.String^ BumpTextureFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Path and file name of the pattern based on an image file for the surface finish

## VBA Syntax

See

[RenderMaterial::BumpTextureFilename](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpTextureFilename.html)

.

## Examples

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)

[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)

[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

## Remarks

This property corresponds to selectingFrom Fileas the surface finish type on the Surface Finish tab of the Appearances PropertyManager page and browsing to an image.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
