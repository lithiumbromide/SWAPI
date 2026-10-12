---
title: "MaterialName Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "MaterialName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~MaterialName.html"
---

# MaterialName Property (ITexture)

Gets or sets the path and file name of the texture material.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.String

instance.MaterialName = value

value = instance.MaterialName
```

### C#

```csharp
System.string MaterialName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name of the texture (see **Remarks**)

## VBA Syntax

See [Texture::MaterialName](ms-its:sldworksapivb6.chm::/sldworks~Texture~MaterialName.html).

## Examples

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html) examples.

## Examples

[Remove Textures From Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

## Remarks

If the texture is a SOLIDWORKS-supplied texture, then the path returned is:

`install_dir`**\data\Images\textures\**texture_library**\**texture_type**\**texture_image_file

For example, `install_dir`\data\Images\textures\plastic\brushed\bred.jpg.

If the texture is user-defined texture, then the path returned is:

drive:**\**`path_name`**\**texture_image_file

For example, D:\MyTextures\gear.jpg.

Call this property before calling [ITexture::GetSystemTextureName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture~GetSystemTextureName.html) to obtain a value for FileNameIn.

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
