---
title: "InsertFilletBeadFeature2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFilletBeadFeature2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature2.html"
---

# InsertFilletBeadFeature2 Method (IFeatureManager)

Inserts a fillet weld bead feature and also fills the gap between the pre-selected part bodies, if any.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFilletBeadFeature2( _
   ByVal Type1 As System.Short, _
   ByVal Size1 As System.Double, _
   ByVal Length1 As System.Double, _
   ByVal PenetrationType1 As System.Short, _
   ByVal PenetrationValue1 As System.Double, _
   ByVal Pitch As System.Double, _
   ByVal Type2 As System.Short, _
   ByVal Size2 As System.Double, _
   ByVal Length2 As System.Double, _
   ByVal PenetrationType2 As System.Short, _
   ByVal PenetrationValue2 As System.Double, _
   ByVal Flag As System.Integer, _
   ByVal EdgeNum1 As System.Integer, _
   ByVal DeSelEdge1 As System.Object, _
   ByVal EdgeNum2 As System.Integer, _
   ByVal DeSelEdge2 As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type1 As System.Short
Dim Size1 As System.Double
Dim Length1 As System.Double
Dim PenetrationType1 As System.Short
Dim PenetrationValue1 As System.Double
Dim Pitch As System.Double
Dim Type2 As System.Short
Dim Size2 As System.Double
Dim Length2 As System.Double
Dim PenetrationType2 As System.Short
Dim PenetrationValue2 As System.Double
Dim Flag As System.Integer
Dim EdgeNum1 As System.Integer
Dim DeSelEdge1 As System.Object
Dim EdgeNum2 As System.Integer
Dim DeSelEdge2 As System.Object
Dim value As Feature

value = instance.InsertFilletBeadFeature2(Type1, Size1, Length1, PenetrationType1, PenetrationValue1, Pitch, Type2, Size2, Length2, PenetrationType2, PenetrationValue2, Flag, EdgeNum1, DeSelEdge1, EdgeNum2, DeSelEdge2)
```

### C#

```csharp
Feature InsertFilletBeadFeature2(
   System.short Type1,
   System.double Size1,
   System.double Length1,
   System.short PenetrationType1,
   System.double PenetrationValue1,
   System.double Pitch,
   System.short Type2,
   System.double Size2,
   System.double Length2,
   System.short PenetrationType2,
   System.double PenetrationValue2,
   System.int Flag,
   System.int EdgeNum1,
   System.object DeSelEdge1,
   System.int EdgeNum2,
   System.object DeSelEdge2
)
```

### C++/CLI

```cpp
Feature^ InsertFilletBeadFeature2(
   System.short Type1,
   System.double Size1,
   System.double Length1,
   System.short PenetrationType1,
   System.double PenetrationValue1,
   System.double Pitch,
   System.short Type2,
   System.double Size2,
   System.double Length2,
   System.short PenetrationType2,
   System.double PenetrationValue2,
   System.int Flag,
   System.int EdgeNum1,
   System.Object^ DeSelEdge1,
   System.int EdgeNum2,
   System.Object^ DeSelEdge2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type1`: First side:

  - 0 = Full length
  - 1 = Intermittent
  - 2 = Staggered
- `Size1`: Size of fillet on first side
- `Length1`: Length of fillet on first side
- `PenetrationType1`: First side:

  - 0 = Full penetration
  - 1 = Partial penetration
  - 2 = No penetration
- `PenetrationValue1`: If penetrationType1 is set to 1 (Partial penetration), then set its value
- `Pitch`: Pitch, if Intermittent or Staggered on both sides
- `Type2`: Second side:

  - 0= Full length
  - 1 = Intermittent
  - 2= Staggered
- `Size2`: Size of fillet on second side
- `Length2`: Length of fillet on second side
- `PenetrationType2`: Second side:

  - 0 = Full penetration
  - 1 = Partial penetration
  - 2 = No penetration
- `PenetrationValue2`: If penetrationType2 is set to 1 (Partial penetration), then set its value
- `Flag`: - 0 = One-sided and no tangent propagation
  - 1 = Two-sided
  - 2 = Tangent propagation
  - 3 = Two-sided and tangent propagation
- `EdgeNum1`: Number of intersecting edges on first side
- `DeSelEdge1`: Array indicating if intersecting edges are selected (0) or deselected (1) on first side
- `EdgeNum2`: Number of intersecting edges on second side
- `DeSelEdge2`: Array indicating if intersecting edges are selected (0) or deselected (1) on second side

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertFilletBeadFeature2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFilletBeadFeature2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IFeatureManager::InsertEndCapFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature.html)
[IFeatureManager::InsertStructuralWeldment2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment2.html)
[IFeatureManager::InsertSubWeldFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder.html)
[IFeatureManager::InsertWeldmentCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList.html)
[IFeatureManager::InsertWeldmentFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentFeature.html)
[IFeatureManager::InsertWeldmentTrimFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.html)
[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html)
[IFeatureManager::InsertFilletBeadFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature3.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
