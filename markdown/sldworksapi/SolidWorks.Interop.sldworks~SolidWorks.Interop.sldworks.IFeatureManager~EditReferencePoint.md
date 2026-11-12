---
title: "EditReferencePoint Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EditReferencePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditReferencePoint.html"
---

# EditReferencePoint Method (IFeatureManager)

Edits the selected reference points.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditReferencePoint( _
   ByVal NRefPointType As System.Integer, _
   ByVal NRefPointAlongCurveType As System.Integer, _
   ByVal DDistance_or_Percent As System.Double, _
   ByVal NumberOfRefPoints As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim NRefPointType As System.Integer
Dim NRefPointAlongCurveType As System.Integer
Dim DDistance_or_Percent As System.Double
Dim NumberOfRefPoints As System.Integer
Dim value As System.Boolean

value = instance.EditReferencePoint(NRefPointType, NRefPointAlongCurveType, DDistance_or_Percent, NumberOfRefPoints)
```

### C#

```csharp
System.bool EditReferencePoint(
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
)
```

### C++/CLI

```cpp
System.bool EditReferencePoint(
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
- `DDistance_or_Percent`: Distance at which to create the reference point on the selected entities or percentage of the length of the selected entities at which to create the reference point if NRefPointAlongCurveType is swRefPointAlongCurveDistance or swRefPointAlongCurvePercentage, respectively
- `NumberOfRefPoints`: Number of reference points to create and evenly distribute on the selected entities if swRefPointAlongCurveType is swRefPointAlongCurveEvenlyDistributed

### Return Value

True if the operation succeeds, false if not

## VBA Syntax

See [FeatureManager::EditReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EditReferencePoint.html).

## Remarks

A reference point is a feature. To programatically create a reference point feature, you can use [IFeatureManager::InsertReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertReferencePoint.html) or [IFeatureManager::IInsertReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertReferencePoint.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
