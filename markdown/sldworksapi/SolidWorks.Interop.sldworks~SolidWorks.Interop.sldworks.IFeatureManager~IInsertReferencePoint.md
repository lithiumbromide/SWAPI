---
title: "IInsertReferencePoint Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IInsertReferencePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertReferencePoint.html"
---

# IInsertReferencePoint Method (IFeatureManager)

Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertReferencePoint( _
   ByVal NRefPointType As System.Integer, _
   ByVal NRefPointAlongCurveType As System.Integer, _
   ByVal DDistance_or_Percent As System.Double, _
   ByVal NumberOfRefPoints As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim NRefPointType As System.Integer
Dim NRefPointAlongCurveType As System.Integer
Dim DDistance_or_Percent As System.Double
Dim NumberOfRefPoints As System.Integer
Dim value As Feature

value = instance.IInsertReferencePoint(NRefPointType, NRefPointAlongCurveType, DDistance_or_Percent, NumberOfRefPoints)
```

### C#

```csharp
Feature IInsertReferencePoint(
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
)
```

### C++/CLI

```cpp
Feature^ IInsertReferencePoint(
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NRefPointType`: Type of reference point as defined by [swRefPointType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointType_e.html)
- `NRefPointAlongCurveType`: Distance, percentage, or evenly distributed as defined by [swRefPointAlongCurveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointAlongCurveType_e.html)
- `DDistance_or_Percent`: Distance at which to create the reference point on the selected entities or percentage of the length of the selected entities at which to create the reference point if nRefPointAlongCurveType is swRefPointAlongCurveDistance or swRefPointAlongCurvePercentage, respectively
- `NumberOfRefPoints`: Number of reference points to create and evenly distribute on the selected entities if swRefPointAlongCurveType is swRefPointAlongCurveEvenlyDistributed

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::IInsertReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~IInsertReferencePoint.html).

## Remarks

This method creates one or more reference point features and adds them to the FeatureManager design tree. If the reference point feature is not created, a NULL value is returned.

The NumberOfRefPoints argument must contain a value of 1 to successfully create one reference point feature. Use the NumberOfRefPoints value to allocate memory for the return value array.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertReferencePoint.html)
[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IFeatureManager::EditReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditReferencePoint.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
