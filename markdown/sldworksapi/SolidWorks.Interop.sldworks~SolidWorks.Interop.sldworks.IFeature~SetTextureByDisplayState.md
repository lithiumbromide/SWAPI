---
title: "SetTextureByDisplayState Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.html"
---

# SetTextureByDisplayState Method (IFeature)

Applies texture to this feature in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTextureByDisplayState( _
   ByVal DisplayStateName As System.String, _
   ByVal TextureIn As Texture _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim DisplayStateName As System.String
Dim TextureIn As Texture
Dim value As System.Boolean

value = instance.SetTextureByDisplayState(DisplayStateName, TextureIn)
```

### C#

```csharp
System.bool SetTextureByDisplayState(
   System.string DisplayStateName,
   Texture TextureIn
)
```

### C++/CLI

```cpp
System.bool SetTextureByDisplayState(
   System.String^ DisplayStateName,
   Texture^ TextureIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Display state name
- `TextureIn`: [Texture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html)

### Return Value

True if the texture is applied to the feature, false if not

## VBA Syntax

See [Feature::SetTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetTextureByDisplayState.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.html)
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.html)
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.html)
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
