---
title: "IGetFirstFacePair Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "IGetFirstFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFacePair.html"
---

# IGetFirstFacePair Method (IMidSurface3)

Gets the first pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstFacePair( _
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

value = instance.IGetFirstFacePair(Thickness, PartnerFaceDisp)
```

### C#

```csharp
Face2 IGetFirstFacePair(
   out System.double Thickness,
   out Face2 PartnerFaceDisp
)
```

### C++/CLI

```cpp
Face2^ IGetFirstFacePair(
   [Out] System.double Thickness,
   [Out] Face2^ PartnerFaceDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Distance between these two parallel faces
- `PartnerFaceDisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

## VBA Syntax

See [MidSurface3::IGetFirstFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~IGetFirstFacePair.html).

## Remarks

The two faces returned by this method are the two parallel faces from the original part body that were used to generate the first neutral face in this midsurface feature.

This method is similar to [IMidSurface3::IGetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetFirstFace.html), except this method does not return the neutral face.

Call [IMidSurface3::IGetNextFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetNextFacePair.html) to get the next pair of faces in this midsurface feature.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFacePairCount.html)
[IMidSurface3::GetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFacePair.html)
[IMidSurface3::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFacePair.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
