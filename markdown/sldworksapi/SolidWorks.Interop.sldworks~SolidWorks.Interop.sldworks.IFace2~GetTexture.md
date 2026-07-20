---
title: "GetTexture Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html"
---

# GetTexture Method (IFace2)

Gets the texture applied to this face in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Config_name As System.String
Dim value As Texture

value = instance.GetTexture(Config_name)
```

### C#

```csharp
Texture GetTexture(
   System.string Config_name
)
```

### C++/CLI

```cpp
Texture^ GetTexture(
   System.String^ Config_name
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Config_name`: Name of the configuration

### Return Value

| If texture is... | Then retval is... |
| --- | --- |
| Applied to this face in Config_name | Pointer to ITexture object |
| Not present | Null |

## VBA Syntax

See

[Face2::GetTexture](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTexture.html)

.

## Examples

[Change Texture on Face in Specified Configuration (VBA)](Change_Texture_on_Face_in_Specified_Configuration_Example_VB.htm)

[Change Texture on Face in Specified Configuration (VB.NET)](Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm)

[Change Texture on Face in Specified Configuration (C#)](Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.html)

[IFace2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.html)

[IFace2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html)

[IFace2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html)

[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
