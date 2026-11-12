---
title: "GetTexture Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture.html"
---

# GetTexture Method (IBody2)

Gets the texture applied to this body in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
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
| Applied to this body in Config_name | Pointer to ITexture object |
| Not present | NULL |

## VBA Syntax

See [Body2::GetTexture](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetTexture.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.html)
[IBody2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.html)
[IBody2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.html)
[IBody2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
