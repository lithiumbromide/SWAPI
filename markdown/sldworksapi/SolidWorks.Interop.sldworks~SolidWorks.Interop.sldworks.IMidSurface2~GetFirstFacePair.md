---
title: "GetFirstFacePair Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "GetFirstFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFacePair.html"
---

# GetFirstFacePair Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::GetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetFirstFacePair.html).

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
Dim instance As IMidSurface2
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

- `Thickness`: Distance between these two parallel faces
- `PartnerFaceDisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face

## VBA Syntax

See [MidSurface2::GetFirstFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~GetFirstFacePair.html).

## Remarks

The two faces returned by this method are the two parallel faces from the original part body that were used to generate the first neutral face in this midsurface feature.

This method is similar to [IMidSurface2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFace.html), except this method does not return the neutral face.

Call [IMidSurface2::GetNextFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetNextFacePair.html) to get the next pair of faces in this midsurface feature.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.html)
[IMidSurface2::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.html)
[IMidSurface2::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
