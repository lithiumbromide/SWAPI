---
title: "SetTexture Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.html"
---

# SetTexture Method (IBody2)

Applies texture to this body in the specified configuration.

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
Dim instance As IBody2
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

- `Config_name`: Name of the configuration
- `TextureIn`: Pointer to the [ITexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html) object

### Return Value

True if texture is applied, false if not

## VBA Syntax

See [Body2::SetTexture](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetTexture.html).

## Examples

[RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.html)
[RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.html)
[IBody2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.html)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture.html)
[IBody2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.html)
[IBody2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.html)
[IBody2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
