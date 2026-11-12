---
title: "RemoveTexture2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RemoveTexture2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html"
---

# RemoveTexture2 Method (IModelDocExtension)

Removes the texture from the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTexture2( _
   ByVal Config_name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Config_name As System.String
Dim value As System.Boolean

value = instance.RemoveTexture2(Config_name)
```

### C#

```csharp
System.bool RemoveTexture2(
   System.string Config_name
)
```

### C++/CLI

```cpp
System.bool RemoveTexture2(
   System.String^ Config_name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_name`: Name of the configuration

### Return Value

True if the texture is removed, false if not

## VBA Syntax

See [ModelDocExtension::RemoveTexture2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RemoveTexture2.html).

## Examples

[Remove Textures from Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.html)
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.html)
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.html)
[IModelDocExtension::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.html)
[IFace2::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
