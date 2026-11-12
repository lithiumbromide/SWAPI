---
title: "SetTexture Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.html"
---

# SetTexture Method (IFeature)

Applies texture to this feature in either all configurations or only the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTexture( _
   ByVal BAllConfig As System.Boolean, _
   ByVal Config_name As System.String, _
   ByVal TextureIn As Texture _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim BAllConfig As System.Boolean
Dim Config_name As System.String
Dim TextureIn As Texture
Dim value As System.Boolean

value = instance.SetTexture(BAllConfig, Config_name, TextureIn)
```

### C#

```csharp
System.bool SetTexture(
   System.bool BAllConfig,
   System.string Config_name,
   Texture TextureIn
)
```

### C++/CLI

```cpp
System.bool SetTexture(
   System.bool BAllConfig,
   System.String^ Config_name,
   Texture^ TextureIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BAllConfig`: True to apply texture to this feature all configurations, false to apply texture to this feature in the configuration specified in config_name only
- `Config_name`: Name of configuration
- `TextureIn`: Pointer to the [ITexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html) object

### Return Value

True if texture is applied, false if not

## VBA Syntax

See [Feature::SetTexture](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetTexture.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.html)
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.html)
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
