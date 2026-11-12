---
title: "GetNextFacePair Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetNextFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFacePair.html"
---

# GetNextFacePair Method (IMidSurface3)

Gets the next pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.

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
Dim instance As IMidSurface3
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

See [MidSurface3::GetNextFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetNextFacePair.html).

## Remarks

The two faces returned are the two parallel faces from the original part body that were used to generate the neutral face in this midsurface feature.

Call [IMidSurface3::GetFirstFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetFirstFacePair.html) to get the first pair of faces used in this midsurface feature.

This method is similar to [IMidSurface3::GetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextFace.html), except this method does not return the neutral face.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFacePair.html)
[IMidSurface3::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFacePairCount.html)
[IMidSurface3::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFacePair.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
