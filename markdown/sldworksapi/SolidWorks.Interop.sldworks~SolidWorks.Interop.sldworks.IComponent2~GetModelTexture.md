---
title: "GetModelTexture Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetModelTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelTexture.html"
---

# GetModelTexture Method (IComponent2)

Gets the texture applied to this lightweight component in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelTexture( _
   ByVal ConfigName As System.String _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ConfigName As System.String
Dim value As Texture

value = instance.GetModelTexture(ConfigName)
```

### C#

```csharp
Texture GetModelTexture(
   System.string ConfigName
)
```

### C++/CLI

```cpp
Texture^ GetModelTexture(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration

### Return Value

[ITexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITexture.html)

## VBA Syntax

See [Component2::GetModelTexture](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetModelTexture.html).

## Examples

[Get Model Textures (VBA)](Get_Model_Texture_Example_VB.htm)
[Get Model Textures (VB.NET)](Get_Model_Texture_Example_VBNET.htm)
[Get Model Textures (C#)](Get_Model_Texture_Example_CSharp.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
