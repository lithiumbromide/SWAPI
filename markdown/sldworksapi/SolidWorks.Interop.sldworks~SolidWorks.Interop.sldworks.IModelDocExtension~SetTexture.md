---
title: "SetTexture Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.html"
---

# SetTexture Method (IModelDocExtension)

Applies texture to the specified configuration.

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
Dim instance As IModelDocExtension
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

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_name`: Name of configuration
- `TextureIn`: [Texture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html)

### Return Value

True if texture is applied, false if not

## VBA Syntax

See [ModelDocExtension::SetTexture](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetTexture.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.html)
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html)
[IModelDocExtension::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.html)
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
