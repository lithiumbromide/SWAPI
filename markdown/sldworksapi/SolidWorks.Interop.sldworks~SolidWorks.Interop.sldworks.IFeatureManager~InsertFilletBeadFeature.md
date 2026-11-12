---
title: "InsertFilletBeadFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFilletBeadFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature.html"
---

# InsertFilletBeadFeature Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertFilletBeadFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFilletBeadFeature( _
   ByVal Type1 As System.Short, _
   ByVal Size1 As System.Double, _
   ByVal Length1 As System.Double, _
   ByVal Pitch As System.Double, _
   ByVal Type2 As System.Short, _
   ByVal Size2 As System.Double, _
   ByVal Length2 As System.Double, _
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
Dim Pitch As System.Double
Dim Type2 As System.Short
Dim Size2 As System.Double
Dim Length2 As System.Double
Dim Flag As System.Integer
Dim EdgeNum1 As System.Integer
Dim DeSelEdge1 As System.Object
Dim EdgeNum2 As System.Integer
Dim DeSelEdge2 As System.Object
Dim value As Feature

value = instance.InsertFilletBeadFeature(Type1, Size1, Length1, Pitch, Type2, Size2, Length2, Flag, EdgeNum1, DeSelEdge1, EdgeNum2, DeSelEdge2)
```

### C#

```csharp
Feature InsertFilletBeadFeature(
   System.short Type1,
   System.double Size1,
   System.double Length1,
   System.double Pitch,
   System.short Type2,
   System.double Size2,
   System.double Length2,
   System.int Flag,
   System.int EdgeNum1,
   System.object DeSelEdge1,
   System.int EdgeNum2,
   System.object DeSelEdge2
)
```

### C++/CLI

```cpp
Feature^ InsertFilletBeadFeature(
   System.short Type1,
   System.double Size1,
   System.double Length1,
   System.double Pitch,
   System.short Type2,
   System.double Size2,
   System.double Length2,
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
- `Pitch`: Pitch, if Intermittent or Staggered on both sides
- `Type2`: Second side:

  - 0= Full length
  - 1 = Intermittent
  - 2= Staggered
- `Size2`: Size of fillet on second side
- `Length2`: Length of fillet on second side
- `Flag`: - 0 = One-sided and no tangent propagation
  - 1 = Two-sided
  - 2 = Tangent propagation
  - 3 = Two-sided and tangent propagation
- `EdgeNum1`: Number of intersecting edges on first side
- `DeSelEdge1`: Array indicating if intersecting edges are selected (0) or deselected (1) on first side
- `EdgeNum2`: Number of intersecting edges on second side
- `DeSelEdge2`: Array indicating if intersecting edges are selected (0) or deselected (1) on second side

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertFilletBeadFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFilletBeadFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
