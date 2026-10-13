---
title: "IGetFirstFace Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "IGetFirstFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetFirstFace.html"
---

# IGetFirstFace Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::IGetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetFirstFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstFace( _
   ByRef FromFace1Disp As Face, _
   ByRef FromFace2Disp As Face, _
   ByRef Thickness As System.Double _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim FromFace1Disp As Face
Dim FromFace2Disp As Face
Dim Thickness As System.Double
Dim value As Face

value = instance.IGetFirstFace(FromFace1Disp, FromFace2Disp, Thickness)
```

### C#

```csharp
Face IGetFirstFace(
   out Face FromFace1Disp,
   out Face FromFace2Disp,
   out System.double Thickness
)
```

### C++/CLI

```cpp
Face^ IGetFirstFace(
   [Out] Face^ FromFace1Disp,
   [Out] Face^ FromFace2Disp,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFace1Disp`:
- `FromFace2Disp`:
- `Thickness`:

## VBA Syntax

See [MidSurface::IGetFirstFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~IGetFirstFace.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
