---
title: "GetTexture Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.html"
---

# GetTexture Method (IComponent2)

Gets the texture applied to this component in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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
| Applied to this component in Config_name | ITexture object |
| Not present | NULL |

## VBA Syntax

See [Component2::GetTexture](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetTexture.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTexture.html)
[IComponent2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTexture.html)
[IComponent2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTextureByDisplayState.html)
[IComponent2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)
[IComponent2::GetModelTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
