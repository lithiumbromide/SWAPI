---
title: "RemoveTextureByDisplayState Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "RemoveTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.html"
---

# RemoveTextureByDisplayState Method (IBody2)

Removes the texture applied to this body in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTextureByDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
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

True if the texture is removed from the body, false if not

## VBA Syntax

See [Body2::RemoveTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Body2~RemoveTextureByDisplayState.html).

## Examples

[Apply and Remove Texture By Body Display State (C#)](Apply_and_Remove_Texture_By_Body_Display_State_Example_CSharp.htm)
[Apply and Remove Texture By Body Display State (VB.NET)](Apply_and_Remove_Texture_By_Body_Display_State_Example_VBNET.htm)
[Apply and Remove Texture By Body Display State (VBA)](Apply_and_Remove_Texture_By_Body_Display_State_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.html)
[IBody2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.html)
[IBody2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.html)
[IBody2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
