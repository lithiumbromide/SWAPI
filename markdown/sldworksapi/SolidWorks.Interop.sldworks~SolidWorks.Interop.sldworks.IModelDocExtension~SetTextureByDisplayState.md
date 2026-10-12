---
title: "SetTextureByDisplayState Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.html"
---

# SetTextureByDisplayState Method (IModelDocExtension)

Sets the texture applied to this model in the specified display state.

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
Dim instance As IModelDocExtension
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

- `DisplayStateName`: Name of display state
- `TextureIn`: [Texture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html)

### Return Value

True if texture is set on the model, false if not

## VBA Syntax

See [ModelDocExtension::SetTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetTextureByDisplayState.html).

## Examples

[Apply and Remove Texture To and From Model by Display State (C#)](Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm)
[Apply and Removed Texture To and From Model By Display State (VB.NET)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm)
[Apply and Remove Texture To and From Model By Display State (VBA)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtenson::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.html)
[IModelDocExtenson::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.html)
[IModelDocExtenson::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html)
[IModelDocExtenson::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.html)
[IModelDocExtenson::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
