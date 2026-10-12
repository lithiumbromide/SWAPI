---
title: "RemoveTexture Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "RemoveTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.html"
---

# RemoveTexture Method (IFeature)

Removes texture from this feature in either all of the configurations or only the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTexture( _
   ByVal BAllConfig As System.Boolean, _
   ByVal Config_name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim BAllConfig As System.Boolean
Dim Config_name As System.String
Dim value As System.Boolean

value = instance.RemoveTexture(BAllConfig, Config_name)
```

### C#

```csharp
System.bool RemoveTexture(
   System.bool BAllConfig,
   System.string Config_name
)
```

### C++/CLI

```cpp
System.bool RemoveTexture(
   System.bool BAllConfig,
   System.String^ Config_name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BAllConfig`: True to remove texture from this feature in all configurations, false to remove texture from this feature in the configuration specified in Config_name only
- `Config_name`: Name of configuration

### Return Value

True if texture is removed, false if not

## VBA Syntax

See [Feature::RemoveTexture](ms-its:sldworksapivb6.chm::/sldworks~Feature~RemoveTexture.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.html)
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.html)
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.html)
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
