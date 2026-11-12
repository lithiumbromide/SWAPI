---
title: "CollectAllCorners Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "CollectAllCorners"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CollectAllCorners.html"
---

# CollectAllCorners Method (ICornerReliefFeatureData)

Creates corners, all with the specified relief, in a selected sheet-metal body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CollectAllCorners( _
   ByVal ReliefType As System.Integer, _
   ByRef Corners As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim ReliefType As System.Integer
Dim Corners As System.Object
Dim value As System.Integer

value = instance.CollectAllCorners(ReliefType, Corners)
```

### C#

```csharp
System.int CollectAllCorners(
   System.int ReliefType,
   out System.object Corners
)
```

### C++/CLI

```cpp
System.int CollectAllCorners(
   System.int ReliefType,
   [Out] System.Object^ Corners
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReliefType`: Corner relief type as defined by [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html)
- `Corners`: Array of [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)s

### Return Value

Error code as defined by [swCornerReliefError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

## VBA Syntax

See [CornerReliefFeatureData::CollectAllCorners](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~CollectAllCorners.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

Before calling this method, call [ICornerReliefFeatureData::SetBodyScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~SetBodyScope.html).

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
