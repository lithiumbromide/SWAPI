---
title: "SetConstraintCurves Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "SetConstraintCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.html"
---

# SetConstraintCurves Method (IFillSurfaceFeatureData)

Sets the entities for the constraint curves.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetConstraintCurves( _
   ByVal ConstraintVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim ConstraintVar As System.Object

instance.SetConstraintCurves(ConstraintVar)
```

### C#

```csharp
void SetConstraintCurves(
   System.object ConstraintVar
)
```

### C++/CLI

```cpp
void SetConstraintCurves(
   System.Object^ ConstraintVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConstraintVar`: Array of entities to use to constrain the surface; valid entities are:

  - [Edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
  - [Sketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [FillSurfaceFeatureData::SetConstraintCurves](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~SetConstraintCurves.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.html)
[IFillSurfaceFeatureData::GetConstraintCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.html)
[IFillSurfaceFeatureData::IGetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetConstraintCurves.html)
[IFillSurfaceFeatureData::ISetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
