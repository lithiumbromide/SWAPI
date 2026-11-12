---
title: "RemoveTexture Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "RemoveTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.html"
---

# RemoveTexture Method (IBody2)

Removes the texture applied to this body in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTexture( _
   ByVal Config_name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
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

See [Body2::RemoveTexture](ms-its:sldworksapivb6.chm::/sldworks~Body2~RemoveTexture.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.html)
[IBody2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture.html)
[IBody2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.html)
[IBody2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
