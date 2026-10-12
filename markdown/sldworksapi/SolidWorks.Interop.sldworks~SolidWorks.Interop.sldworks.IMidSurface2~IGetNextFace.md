---
title: "IGetNextFace Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "IGetNextFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFace.html"
---

# IGetNextFace Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::IGetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetNextFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNextFace( _
   ByRef FromFace1Disp As Face2, _
   ByRef FromFace2Disp As Face2, _
   ByRef Thickness As System.Double _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim FromFace1Disp As Face2
Dim FromFace2Disp As Face2
Dim Thickness As System.Double
Dim value As Face2

value = instance.IGetNextFace(FromFace1Disp, FromFace2Disp, Thickness)
```

### C#

```csharp
Face2 IGetNextFace(
   out Face2 FromFace1Disp,
   out Face2 FromFace2Disp,
   out System.double Thickness
)
```

### C++/CLI

```cpp
Face2^ IGetNextFace(
   [Out] Face2^ FromFace1Disp,
   [Out] Face2^ FromFace2Disp,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFace1Disp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face
- `FromFace2Disp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face
- `Thickness`: Distance between the two parallel faces, FromFace1Disp and FromFace2Disp

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in this midsurface feature

## VBA Syntax

See [MidSurface2::IGetNextFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~IGetNextFace.html).

## Remarks

Call [IMidSurface2::IGetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetFirstFace.html) before calling this method to get the first neutral face.

This method returns the next neutral face in this midsurface feature along with three other items.

- The first two return values are the two faces from the original part body that were used to generate this neutral midsurface face.
- The next return value is the thickness (in meters) between the two parallel faces from the original part body.
- The last return value is the neutral face in this midsurface feature.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFace.html)
[IMidSurface2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFaceCount.html)
[IMidSurface2::GetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
