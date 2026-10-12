---
title: "SetTexture Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTexture.html"
---

# SetTexture Method (IComponent2)

Applies texture to this component in the specified configuration.

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
Dim instance As IComponent2
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
- `TextureIn`: Pointer to the [ITexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html) object

### Return Value

True if texture is applied, false if not

## VBA Syntax

See [Component2::SetTexture](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetTexture.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.html)
[IComponent2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTexture.html)
[IComponent2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTextureByDisplayState.html)
[IComponent2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
