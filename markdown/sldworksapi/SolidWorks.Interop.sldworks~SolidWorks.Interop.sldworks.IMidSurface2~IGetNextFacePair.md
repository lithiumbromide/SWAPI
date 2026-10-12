---
title: "IGetNextFacePair Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "IGetNextFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.html"
---

# IGetNextFacePair Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::IGetNextFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetNextFacePair.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNextFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As Face2 _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim Thickness As System.Double
Dim PartnerFaceDisp As Face2
Dim value As Face2

value = instance.IGetNextFacePair(Thickness, PartnerFaceDisp)
```

### C#

```csharp
Face2 IGetNextFacePair(
   out System.double Thickness,
   out Face2 PartnerFaceDisp
)
```

### C++/CLI

```cpp
Face2^ IGetNextFacePair(
   [Out] System.double Thickness,
   [Out] Face2^ PartnerFaceDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Distance between theses two parallel faces
- `PartnerFaceDisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

## VBA Syntax

See [MidSurface2::IGetNextFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~IGetNextFacePair.html).

## Remarks

The two faces returned are the two parallel faces from the original part body that were used to generate the neutral face in this midsurface feature.

Call [IMidSurface2::IGetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetFirstFacePair.html) to get the first pair of faces used in this midsurface feature.

This method is similar to [IMidSurface2::IGetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetNextFace.html), except this method does not return the neutral face.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::GetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFacePair.html)
[IMidSurface2::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.html)
[IMidSurface2::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
