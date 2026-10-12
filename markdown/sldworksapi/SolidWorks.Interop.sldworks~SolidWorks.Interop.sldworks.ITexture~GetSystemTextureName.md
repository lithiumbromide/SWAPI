---
title: "GetSystemTextureName Method (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "GetSystemTextureName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~GetSystemTextureName.html"
---

# GetSystemTextureName Method (ITexture)

Gets the name of the texture that appears in the Texture PropertyManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSystemTextureName( _
   ByVal FileNameIn As System.String, _
   ByRef Res As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim FileNameIn As System.String
Dim Res As System.Boolean
Dim value As System.String

value = instance.GetSystemTextureName(FileNameIn, Res)
```

### C#

```csharp
System.string GetSystemTextureName(
   System.string FileNameIn,
   out System.bool Res
)
```

### C++/CLI

```cpp
System.String^ GetSystemTextureName(
   System.String^ FileNameIn,
   [Out] System.bool Res
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileNameIn`: Path and filename of texture (see **Remarks**)
- `Res`: True if the name of the texture that appears in the Texture PropertyManager is returned, false if not

### Return Value

Name of texture as it appears in the Texture PropertyManager (see Remarks)

## VBA Syntax

See [Texture::GetSystemTextureName](ms-its:sldworksapivb6.chm::/sldworks~Texture~GetSystemTextureName.html).

## Examples

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html) examples.

## Remarks

This method only supports SOLIDWORKS-supplied textures.

Call [ITexture::MaterialName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture~MaterialName.html) to get the value for FileNameIn before calling this method. ITexture::MaterialName returns an abbreviated path and the name of the texture as it appears in the Texture PropertyManager. For example, if ITexture::MaterialName returns `install_dir`**\data\images\textures\plastic\brushed\bred.jpg**, then this method returns Plastic\Brushed\Red.

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
