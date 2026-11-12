---
title: "GetFaces Method (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "GetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~GetFaces.html"
---

# GetFaces Method (ISMCornerReliefData)

Gets the faces used to create this sheet metal corner.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFaces( _
   ByRef Face1 As System.Object, _
   ByRef Face2 As System.Object, _
   ByRef Face3 As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim Face1 As System.Object
Dim Face2 As System.Object
Dim Face3 As System.Object

instance.GetFaces(Face1, Face2, Face3)
```

### C#

```csharp
void GetFaces(
   out System.object Face1,
   out System.object Face2,
   out System.object Face3
)
```

### C++/CLI

```cpp
void GetFaces(
   [Out] System.Object^ Face1,
   [Out] System.Object^ Face2,
   [Out] System.Object^ Face3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Face1`: First [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) that defines this two- or three-bend corner
- `Face2`: Second IFace2 that defines this two- or three-bend corner
- `Face3`: Third IFace2 that defines this three-bend corner; valid only if ICornerReliefFeatureData::CornerReliefBendType is [swCornerReliefBendType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html).swCornerReliefBendType_ThreeBend; specify null or Nothing for a two-bend corner

## VBA Syntax

See [SMCornerReliefData::GetFaces](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~GetFaces.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
