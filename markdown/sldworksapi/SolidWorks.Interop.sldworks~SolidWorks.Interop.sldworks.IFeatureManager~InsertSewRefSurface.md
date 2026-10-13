---
title: "InsertSewRefSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSewRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSewRefSurface.html"
---

# InsertSewRefSurface Method (IFeatureManager)

Creates a surface by knitting the selected surfaces together.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSewRefSurface( _
   ByVal UseGapFilters As System.Boolean, _
   ByVal TryToFormSolid As System.Boolean, _
   ByVal MergeEntities As System.Boolean, _
   ByVal KnitTolerance As System.Double, _
   ByVal MaxValueForGapRange As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim UseGapFilters As System.Boolean
Dim TryToFormSolid As System.Boolean
Dim MergeEntities As System.Boolean
Dim KnitTolerance As System.Double
Dim MaxValueForGapRange As System.Double
Dim value As Feature

value = instance.InsertSewRefSurface(UseGapFilters, TryToFormSolid, MergeEntities, KnitTolerance, MaxValueForGapRange)
```

### C#

```csharp
Feature InsertSewRefSurface(
   System.bool UseGapFilters,
   System.bool TryToFormSolid,
   System.bool MergeEntities,
   System.double KnitTolerance,
   System.double MaxValueForGapRange
)
```

### C++/CLI

```cpp
Feature^ InsertSewRefSurface(
   System.bool UseGapFilters,
   System.bool TryToFormSolid,
   System.bool MergeEntities,
   System.double KnitTolerance,
   System.double MaxValueForGapRange
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseGapFilters`: True to use gap filters, false to not
- `TryToFormSolid`: True to form a solid body, false to no
- `MergeEntities`: True to merge edges and faces by removing redundant vertices and edges, false to not
- `KnitTolerance`: Knit tolerance (see **Remarks**)
- `MaxValueForGapRange`: Maximum value of gap range for gap filters

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertSewRefSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSewRefSurface.html).

## Examples

[Create Surface Knit Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)
[Create Surface Knit Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)
[Create Surface Knit Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

## Remarks

Make selections using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark number of 1. See the SOLIDWORKS Help for information about what entities are valid for selection.

A knit tolerance's:

- lower limit is 0.0001 mm
- upper limit is 0.1 mm

The knit tolerance value should be in a gap range such that:

(Minimum gap) <= (Knit tolerance) <= MIN(0.1 mm, Maximum gap)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
