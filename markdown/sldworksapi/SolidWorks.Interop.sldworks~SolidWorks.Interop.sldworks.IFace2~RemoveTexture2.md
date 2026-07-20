---
title: "RemoveTexture2 Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "RemoveTexture2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.html"
---

# RemoveTexture2 Method (IFace2)

Removes the texture applied to this face in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTexture2( _
   ByVal Config_name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Config_name`: Name of the configuration

### Return Value

True if texture is removed, false if not

## VBA Syntax

See

[Face2::RemoveTexture2](ms-its:sldworksapivb6.chm::/sldworks~Face2~RemoveTexture2.html)

.

## Examples

[Apply and Remove Texture (VBA)](Apply_and_Remove_Texture_By_Configuration_Example_VB.htm)

[Apply and Remove Texture (VB.NET)](Apply_and_Remove_Texture_By_Configuration_Example_VBNET.htm)

[Apply and Remove Texture (C#)](Apply_and_Remove_Texture_By_Configuration_Example_CSharp.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html)

[IFace2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.html)

[IFace2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html)

[IFace2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html)

[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2013 SP02, Revision Number 21.2
