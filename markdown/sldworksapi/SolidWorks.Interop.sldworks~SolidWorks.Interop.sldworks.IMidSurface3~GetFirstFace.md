---
title: "GetFirstFace Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetFirstFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFace.html"
---

# GetFirstFace Method (IMidSurface3)

Gets the first face in this midsurface feature and three other items.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFace( _
   ByRef FromFace1Disp As System.Object, _
   ByRef FromFace2Disp As System.Object, _
   ByRef Thickness As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim FromFace1Disp As System.Object
Dim FromFace2Disp As System.Object
Dim Thickness As System.Double
Dim value As System.Object

value = instance.GetFirstFace(FromFace1Disp, FromFace2Disp, Thickness)
```

### C#

```csharp
System.object GetFirstFace(
   out System.object FromFace1Disp,
   out System.object FromFace2Disp,
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetFirstFace(
   [Out] System.Object^ FromFace1Disp,
   [Out] System.Object^ FromFace2Disp,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFace1Disp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original part body used in generating the neutral face
- `FromFace2Disp`: Parallel [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to FromFace1Disp on the original part body used in generating the neutral face
- `Thickness`: Distance between the two parallel faces, FromFace1Disp and FromFace2Disp

### Return Value

First [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in this midsurface feature

## VBA Syntax

See [MidSurface3::GetFirstFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetFirstFace.html).

## Remarks

- The first two return values are the two faces from the original part body that were used to generate this midsurface face.
- The next return value is the thickness (in meters) between the two parallel faces from the original part body.
- The last return value is the first face in this midsurface feature.

Use [IMidSurface3::GetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextFace.html) to get the next neutral face in this midsurface feature.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaceCount.html)
[IMidSurface3::GetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFace.html)
[IMidSurface3::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFace.html)
[IMidSurface3::IGetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFace.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
