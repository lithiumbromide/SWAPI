---
title: "ITexture Interface"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html"
---

# ITexture Interface

Use to apply 2D textures to part and assembly documents for a more realistic finish.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITexture
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
```

### C#

```csharp
public interface ITexture
```

### C++/CLI

```cpp
public interface class ITexture
```

## VBA Syntax

See [Texture](ms-its:sldworksapivb6.chm::/sldworks~Texture.html).

## Examples

[Change Texture on Face in Specified Configuration (VBA)](Change_Texture_on_Face_in_Specified_Configuration_Example_VB.htm)
[Change Texture on Face in Specified Configuration (VB.NET)](Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm)
[Change Texture on Face in Specified Configuration (C#)](Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm)

## Remarks

To get or set the location of a texture file, use [ISldWorks::GetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html) or [ISldWorks::SetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html) and swFileLocationsTextures.

## Accessors

[IBody2::GetTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetTexture.html)

[IComponent2::GetModelTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelTexture.html)

[IComponent2::GetTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetTexture.html)

[IFace2::GetTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTexture.html)

[IFeature::GetTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTexture.html)

[IModelDocExtension::CreateTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateTexture.html)

[IModelDocExtension::GetTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetTexture.html)

## Access Diagram

[Texture](SWObjectModel.pdf#Texture)

## See Also

[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
