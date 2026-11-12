---
title: "RemoveTexture Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "RemoveTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTexture.html"
---

# RemoveTexture Method (IComponent2)

Removes the texture from this component in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTexture( _
   ByVal Config_name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Config_name As System.String
Dim value As System.Boolean

value = instance.RemoveTexture(Config_name)
```

### C#

```csharp
System.bool RemoveTexture(
   System.string Config_name
)
```

### C++/CLI

```cpp
System.bool RemoveTexture(
   System.String^ Config_name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_name`: Name of the configuration

### Return Value

True if texture is removed, false if not

## VBA Syntax

See [Component2::RemoveTexture](ms-its:sldworksapivb6.chm::/sldworks~Component2~RemoveTexture.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.html)
[IComponent2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTexture.html)
[IComponent2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTextureByDisplayState.html)
[IComponent2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
