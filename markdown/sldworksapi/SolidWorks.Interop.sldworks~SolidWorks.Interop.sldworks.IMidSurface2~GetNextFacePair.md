---
title: "GetNextFacePair Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "GetNextFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.html"
---

# GetNextFacePair Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::GetNextFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextFacePair.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim Thickness As System.Double
Dim PartnerFaceDisp As System.Object
Dim value As System.Object

value = instance.GetNextFacePair(Thickness, PartnerFaceDisp)
```

### C#

```csharp
System.object GetNextFacePair(
   out System.double Thickness,
   out System.object PartnerFaceDisp
)
```

### C++/CLI

```cpp
System.Object^ GetNextFacePair(
   [Out] System.double Thickness,
   [Out] System.Object^ PartnerFaceDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Distance between theses two parallel faces
- `PartnerFaceDisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

## VBA Syntax

See [MidSurface2::GetNextFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~GetNextFacePair.html).

## Remarks

The two faces returned are the two parallel faces from the original part body that were used to generate the neutral face in this midsurface feature.

Call [IMidSurface2::GetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFacePair.html) to get the first pair of faces used in this midsurface feature.

This method is similar to [IMidSurface2::GetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetNextFace.html), except this method does not return the neutral face.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.html)
[IMidSurface2::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.html)
[IMidSurface2::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
