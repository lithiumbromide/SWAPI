---
title: "GetFirstFacePair Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetFirstFacePair"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFacePair.html"
---

# GetFirstFacePair Method (IMidSurface3)

Gets the first pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.

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
Dim instance As IMidSurface3
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

See [MidSurface3::GetFirstFacePair](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetFirstFacePair.html).

## Remarks

The two faces returned by this method are the two parallel faces from the original part body that were used to generate the first neutral face in this midsurface feature.

This method is similar to [IMidSurface3::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetFirstFace.html), except this method does not return the neutral face.

Call [IMidSurface3::GetNextFacePair](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextFacePair.html) to get the next pair of faces in this midsurface feature.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.html)
[IMidSurface3::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.html)
[IMidSurface3::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.html)
[IMidSurface3::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
