---
title: "RemoveTextureByDisplayState Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RemoveTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.html"
---

# RemoveTextureByDisplayState Method (IModelDocExtension)

Removes the texture applied to this model in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTextureByDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
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

- `DisplayStateName`: Name of display state

### Return Value

True if texture removed from model, false if not

## VBA Syntax

See [ModelDocExtension::RemoveTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RemoveTextureByDisplayState.html).

## Examples

[Apply and Remove Texture To and From Model By Display State (C#)](Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm)
[Apply and Remove Texture To and From Model By Display State (VB.NET)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm)
[Apply and Remove Texture To and From Model By Display State (VBA)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.html)
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html)
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.html)
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.html)
[IModelDocExtenson::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
