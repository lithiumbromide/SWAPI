---
title: "SetTextureByDisplayState Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTextureByDisplayState.html"
---

# SetTextureByDisplayState Method (IComponent2)

Sets the texture applied to this component in the specified display state.

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
Dim instance As IComponent2
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

True if texture is applied to the component, false if not

## VBA Syntax

See [Component2::SetTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetTextureByDisplayState.html).

## Examples

[Apply and Remove Texture To and From Component By Display State (C#)](Apply_and_Remove_Texture_By_Component_Display_State_Example_CSharp.htm)
[Apply and Remove Texture To and From Component By Display State (VB.NET)](Apply_and_Remove_Texture_By_Component_Display_State_Example_VBNET.htm)
[Apply and Remove Texture To and From Component By Display State (VBA)](Apply_and_Remove_Texture_By_Component_Display_State_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTextureByDisplayState.html)
[IComponent2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTexture.html)
[IComponent2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTexture.html)
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
