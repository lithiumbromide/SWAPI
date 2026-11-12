---
title: "IGetSurface Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.html"
---

# IGetSurface Method (IFace2)

Gets the surface referenced by this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSurface() As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Surface

value = instance.IGetSurface()
```

### C#

```csharp
Surface IGetSurface()
```

### C++/CLI

```cpp
Surface^ IGetSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the underlying [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) for this face

## VBA Syntax

See [Face2::IGetSurface](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetSurface.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.html)
[IFace2::AttachSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AttachSurface.html)
[IFace2::DetachSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~DetachSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
