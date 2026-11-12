---
title: "RemoveTexture Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "RemoveTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture.html"
---

# RemoveTexture Method (IFace2)

Obsolete. Superseded by [IFace2::RemoveTexture2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~RemoveTexture2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTexture( _
   ByVal Config_name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

See [Face2::RemoveTexture](ms-its:sldworksapivb6.chm::/sldworks~Face2~RemoveTexture.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html)
[IFace2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.html)
[IFace2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html)
[IFace2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
