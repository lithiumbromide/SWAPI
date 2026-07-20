---
title: "AttachSurface Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "AttachSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AttachSurface.html"
---

# AttachSurface Method (IFace2)

Attaches a surface to this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function AttachSurface( _
   ByVal SurfIn As Surface, _
   ByVal SenseIn As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim SurfIn As Surface
Dim SenseIn As System.Boolean
Dim value As System.Boolean

value = instance.AttachSurface(SurfIn, SenseIn)
```

### C#

```csharp
System.bool AttachSurface(
   Surface SurfIn,
   System.bool SenseIn
)
```

### C++/CLI

```cpp
System.bool AttachSurface(
   Surface^ SurfIn,
   System.bool SenseIn
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `SurfIn`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

to attach to face
- `SenseIn`: True if surface normal and face normal are in the same direction, false if surface normal and face normal are in opposite direction

### Return Value

True if surface is attached to face, false if notParamDesc

## VBA Syntax

See

[Face2::AttachSurface](ms-its:sldworksapivb6.chm::/sldworks~Face2~AttachSurface.html)

.

## Remarks

To detach surfaces from faces, use[IFace2::DetachSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~DetachSurface.html). Neither IFace2::AttachSurface nor IFace2::DetachSurface affect body topology.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::GetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.html)

[IFace2::IGetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
