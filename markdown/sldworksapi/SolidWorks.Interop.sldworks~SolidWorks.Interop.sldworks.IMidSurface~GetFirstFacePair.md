---
title: "GetFirstFacePair Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "GetFirstFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetFirstFacePair.html"
---

# GetFirstFacePair Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::GetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFacePair.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim Thickness As System.Double
Dim PartnerFaceDisp As System.Object
Dim value As System.Object

value = instance.GetFirstFacePair(Thickness, PartnerFaceDisp)
```

### C#

```csharp
System.object GetFirstFacePair(
   out System.double Thickness,
   out System.object PartnerFaceDisp
)
```

### C++/CLI

```cpp
System.Object^ GetFirstFacePair(
   [Out] System.double Thickness,
   [Out] System.Object^ PartnerFaceDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `PartnerFaceDisp`:

## VBA Syntax

See [MidSurface::GetFirstFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~GetFirstFacePair.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
