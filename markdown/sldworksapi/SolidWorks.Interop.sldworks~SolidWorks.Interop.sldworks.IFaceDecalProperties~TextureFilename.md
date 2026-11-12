---
title: "TextureFilename Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureFilename"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureFilename.html"
---

# TextureFilename Property (IFaceDecalProperties)

Gets the file name of the texture of the decal.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureFilename As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.String

value = instance.TextureFilename
```

### C#

```csharp
System.string TextureFilename {get;}
```

### C++/CLI

```cpp
property System.String^ TextureFilename {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fully qualified path and file name of the texture

## VBA Syntax

See [FaceDecalProperties::TextureFilename](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureFilename.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)
[IFaceDecalProperties::TextureFilenameID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureFilenameID.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
