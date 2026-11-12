---
title: "GetConstraintCurves Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "GetConstraintCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.html"
---

# GetConstraintCurves Method (IFillSurfaceFeatureData)

Gets the constraint curves for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstraintCurves( _
   ByRef TypeArr As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim TypeArr As System.Object
Dim value As System.Object

value = instance.GetConstraintCurves(TypeArr)
```

### C#

```csharp
System.object GetConstraintCurves(
   out System.object TypeArr
)
```

### C++/CLI

```cpp
System.Object^ GetConstraintCurves(
   [Out] System.Object^ TypeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TypeArr`: Array of types of entities used to constrain the surface as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html); valid entities are:

  - edges (swSelEDGES)
  - sketches (swSelSKETCHES)

### Return Value

Array of entities used as constraint curves

## VBA Syntax

See [FillSurfaceFeatureData::GetConstraintCurves](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~GetConstraintCurves.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::IGetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetConstraintCurves.html)
[IFillSurfaceFeatureData::GetConstraintCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.html)
[IFillSurfaceFeatureData::SetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.html)
[IFillSurfaceFeatureData::ISetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
