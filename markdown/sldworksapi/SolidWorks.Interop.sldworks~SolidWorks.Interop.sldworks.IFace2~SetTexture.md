---
title: "SetTexture Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "SetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.html"
---

# SetTexture Method (IFace2)

Applies texture to this face in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTexture( _
   ByVal Config_name As System.String, _
   ByVal TextureIn As Texture _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Config_name As System.String
Dim TextureIn As Texture
Dim value As System.Boolean

value = instance.SetTexture(Config_name, TextureIn)
```

### C#

```csharp
System.bool SetTexture(
   System.string Config_name,
   Texture TextureIn
)
```

### C++/CLI

```cpp
System.bool SetTexture(
   System.String^ Config_name,
   Texture^ TextureIn
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Config_name`: Name of configuration
- `TextureIn`: [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)ParamDesc

### Return Value

True if texture is applied, false if notParamDesc

## VBA Syntax

See

[Face2::SetTexture](ms-its:sldworksapivb6.chm::/sldworks~Face2~SetTexture.html)

.

## Examples

[Change Texture on Face in Specified Configuration (VBA)](Change_Texture_on_Face_in_Specified_Configuration_Example_VB.htm)

[Change Texture on Face in Specified Configuration (VB.NET)](Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm)

[Change Texture on Face in Specified Configuration (C#)](Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html)

[IFace2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture.html)

[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

[IFace2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html)

[IFace2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
