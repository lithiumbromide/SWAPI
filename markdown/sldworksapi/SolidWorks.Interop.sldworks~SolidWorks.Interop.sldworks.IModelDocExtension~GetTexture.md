---
title: "GetTexture Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.html"
---

# GetTexture Method (IModelDocExtension)

Gets the texture applied to the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
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

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_name`: Name of configuration or NULL if texture is not present

### Return Value

[Texture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html)

## VBA Syntax

See [ModelDocExtension::GetTexture](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetTexture.html).

## Examples

[Remove Textures from Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html)
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.html)
[IModelDocExtension::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.html)
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
