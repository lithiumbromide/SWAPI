---
title: "IGetNextFacePair Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "IGetNextFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetNextFacePair.html"
---

# IGetNextFacePair Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::IGetNextFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetNextFacePair.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNextFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As Face _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim Thickness As System.Double
Dim PartnerFaceDisp As Face
Dim value As Face

value = instance.IGetNextFacePair(Thickness, PartnerFaceDisp)
```

### C#

```csharp
Face IGetNextFacePair(
   out System.double Thickness,
   out Face PartnerFaceDisp
)
```

### C++/CLI

```cpp
Face^ IGetNextFacePair(
   [Out] System.double Thickness,
   [Out] Face^ PartnerFaceDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `PartnerFaceDisp`:

## VBA Syntax

See [MidSurface::IGetNextFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~IGetNextFacePair.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
