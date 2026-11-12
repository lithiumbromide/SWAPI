---
title: "AddNewCorner Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "AddNewCorner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~AddNewCorner.html"
---

# AddNewCorner Method (ICornerReliefFeatureData)

Adds a corner with the specified parameters to this sheet metal corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddNewCorner( _
   ByVal Face1 As System.Object, _
   ByVal Face2 As System.Object, _
   ByVal Face3 As System.Object, _
   ByVal ReliefType As System.Integer, _
   ByRef Corner As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim Face1 As System.Object
Dim Face2 As System.Object
Dim Face3 As System.Object
Dim ReliefType As System.Integer
Dim Corner As System.Object
Dim value As System.Integer

value = instance.AddNewCorner(Face1, Face2, Face3, ReliefType, Corner)
```

### C#

```csharp
System.int AddNewCorner(
   System.object Face1,
   System.object Face2,
   System.object Face3,
   System.int ReliefType,
   out System.object Corner
)
```

### C++/CLI

```cpp
System.int AddNewCorner(
   System.Object^ Face1,
   System.Object^ Face2,
   System.Object^ Face3,
   System.int ReliefType,
   [Out] System.Object^ Corner
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Face1`: First [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) that defines this two- or three-bend corner
- `Face2`: Second IFace2 that defines this two- or three-bend corner
- `Face3`: Third IFace2 that defines this three-bend corner; valid only if ICornerReliefFeatureData::CornerReliefBendType is [swCornerReliefBendType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html).swCornerReliefBendType_ThreeBend; specify null or Nothing for a two-bend corner
- `ReliefType`: Corner relief type as defined by [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html)
- `Corner`: [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)

### Return Value

Error code as defined by [swCornerReliefError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

## VBA Syntax

See [CornerReliefFeatureData::AddNewCorner](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~AddNewCorner.html).

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
