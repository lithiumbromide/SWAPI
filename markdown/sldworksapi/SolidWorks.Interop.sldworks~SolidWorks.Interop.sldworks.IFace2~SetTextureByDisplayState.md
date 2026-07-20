---
title: "SetTextureByDisplayState Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "SetTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html"
---

# SetTextureByDisplayState Method (IFace2)

Applies texture to this face in the specified display state.

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
Dim instance As IFace2
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

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `DisplayStateName`: Display state name
- `TextureIn`: [Texture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html)

### Return Value

True if texture applied to face, false if not

## VBA Syntax

See

[Face2::SetTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Face2~SetTextureByDisplayState.html)

.

## Examples

[Apply and Remove Texture By Display State (C#)](Apply_and_Remove_Texture_By_Display_State_Example_CSharp.htm)

[Apply and Remove Texture By Display State (VB.NET)](Apply_and_Remove_Texture_By_Display_State_Example_VBNET.htm)

[Apply and Remove Texture By Display State (VBA)](Apply_and_Remove_Texture_By_Display_State_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html)

[IFace2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture.html)

[IFace2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.html)

[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

[IFace2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
