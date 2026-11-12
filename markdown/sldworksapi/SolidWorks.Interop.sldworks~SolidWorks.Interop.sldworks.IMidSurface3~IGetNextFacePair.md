---
title: "IGetNextFacePair Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "IGetNextFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFacePair.html"
---

# IGetNextFacePair Method (IMidSurface3)

Gets the next pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.

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
Dim instance As IMidSurface3
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

See [MidSurface3::IGetNextFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~IGetNextFacePair.html).

## Remarks

The two faces returned are the two parallel faces from the original part body that were used to generate the neutral face in this midsurface feature.

Call [IMidSurface3::IGetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetFirstFacePair.html) to get the first pair of faces used in this midsurface feature.

This method is similar to [IMidSurface3::IGetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetNextFace.html), except this method does not return the neutral face.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFacePairCount.html)
[IMidSurface3::GetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFacePair.html)
[IMidSurface3::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFacePair.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
