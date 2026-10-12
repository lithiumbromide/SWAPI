---
title: "TextureMirrored Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureMirrored"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureMirrored.html"
---

# TextureMirrored Property (IFaceDecalProperties)

Gets whether the texture of the decal is mirrored.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureMirrored As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Boolean

value = instance.TextureMirrored
```

### C#

```csharp
System.bool TextureMirrored {get;}
```

### C++/CLI

```cpp
property System.bool TextureMirrored {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the texture of the decal is mirrored, false if not

## VBA Syntax

See [FaceDecalProperties::TextureMirrored](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureMirrored.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
