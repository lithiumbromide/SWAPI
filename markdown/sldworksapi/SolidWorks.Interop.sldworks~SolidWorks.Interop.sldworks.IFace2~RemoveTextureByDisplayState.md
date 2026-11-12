---
title: "RemoveTextureByDisplayState Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "RemoveTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html"
---

# RemoveTextureByDisplayState Method (IFace2)

Removes the texture applied to this face in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTextureByDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim DisplayStateName As System.String
Dim value As System.Boolean

value = instance.RemoveTextureByDisplayState(DisplayStateName)
```

### C#

```csharp
System.bool RemoveTextureByDisplayState(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
System.bool RemoveTextureByDisplayState(
   System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Display state name

### Return Value

True if the texture is removed, false if not

## VBA Syntax

See [Face2::RemoveTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Face2~RemoveTextureByDisplayState.html).

## Examples

[Apply and Remove Texture By Display State (C#)](Apply_and_Remove_Texture_By_Display_State_Example_CSharp.htm)
[Apply and Remove Texture By Display State (VB.NET)](Apply_and_Remove_Texture_By_Display_State_Example_VBNET.htm)
[Apply and Remove Texture By Display State (VBA)](Apply_and_Remove_Texture_By_Display_State_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html)
[IFace2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.html)
[IFace2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture.html)
[IFace2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
