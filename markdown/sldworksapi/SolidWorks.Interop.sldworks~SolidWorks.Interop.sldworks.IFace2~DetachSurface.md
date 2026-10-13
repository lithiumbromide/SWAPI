---
title: "DetachSurface Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "DetachSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~DetachSurface.html"
---

# DetachSurface Method (IFace2)

Detaches a surface from this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function DetachSurface() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Boolean

value = instance.DetachSurface()
```

### C#

```csharp
System.bool DetachSurface()
```

### C++/CLI

```cpp
System.bool DetachSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the surface is detached from this face, false if not

## VBA Syntax

See [Face2::DetachSurface](ms-its:sldworksapivb6.chm::/sldworks~Face2~DetachSurface.html).

## Examples

Use[IFace2::AttachSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~AttachSurface.html) to attach surfaces to faces. Neither IFace2::DetachFace nor IFace2::AttachFace affect body topology.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.html)
[IFace2::GetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
