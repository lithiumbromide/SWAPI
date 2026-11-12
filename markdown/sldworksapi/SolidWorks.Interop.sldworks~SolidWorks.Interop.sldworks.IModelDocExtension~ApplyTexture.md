---
title: "ApplyTexture Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ApplyTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ApplyTexture.html"
---

# ApplyTexture Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::SetTexture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetTexture.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyTexture( _
   ByVal Scale As System.Integer, _
   ByVal Angle As System.Double, _
   ByVal TextureFilename As System.String, _
   ByVal BlendColor As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Scale As System.Integer
Dim Angle As System.Double
Dim TextureFilename As System.String
Dim BlendColor As System.Boolean
Dim value As System.Boolean

value = instance.ApplyTexture(Scale, Angle, TextureFilename, BlendColor)
```

### C#

```csharp
System.bool ApplyTexture(
   System.int Scale,
   System.double Angle,
   System.string TextureFilename,
   System.bool BlendColor
)
```

### C++/CLI

```cpp
System.bool ApplyTexture(
   System.int Scale,
   System.double Angle,
   System.String^ TextureFilename,
   System.bool BlendColor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scale`:
- `Angle`:
- `TextureFilename`:
- `BlendColor`:

## VBA Syntax

See [ModelDocExtension::ApplyTexture](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ApplyTexture.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
