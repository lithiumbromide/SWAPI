---
title: "GetTexture Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.html"
---

# GetTexture Method (IFeature)

Gets the texture applied to this feature in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
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

- `Config_name`: Name of the configuration

### Return Value

| If texture is... | Then retval is... |
| --- | --- |
| Applied to this feature in Cofig_name | Pointer to ITexture object |
| Not present | NULL |

## VBA Syntax

See [Feature::GetTexture](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetTexture.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.html)
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.html)
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.html)
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
