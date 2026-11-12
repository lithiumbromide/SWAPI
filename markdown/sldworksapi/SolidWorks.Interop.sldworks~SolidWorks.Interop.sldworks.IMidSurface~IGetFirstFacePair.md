---
title: "IGetFirstFacePair Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "IGetFirstFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetFirstFacePair.html"
---

# IGetFirstFacePair Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::IGetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetFirstFacePair.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstFacePair( _
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

value = instance.IGetFirstFacePair(Thickness, PartnerFaceDisp)
```

### C#

```csharp
Face IGetFirstFacePair(
   out System.double Thickness,
   out Face PartnerFaceDisp
)
```

### C++/CLI

```cpp
Face^ IGetFirstFacePair(
   [Out] System.double Thickness,
   [Out] Face^ PartnerFaceDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `PartnerFaceDisp`:

## VBA Syntax

See [MidSurface::IGetFirstFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~IGetFirstFacePair.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
