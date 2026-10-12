---
title: "ISetConstraintCurves Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "ISetConstraintCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.html"
---

# ISetConstraintCurves Method (IFillSurfaceFeatureData)

Sets the entities for the constraint curves.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetConstraintCurves( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object

instance.ISetConstraintCurves(Count, DispArr)
```

### C#

```csharp
void ISetConstraintCurves(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
void ISetConstraintCurves(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities to use to constrain the surface
- `DispArr`: - in-process, unmanaged C++: Pointer to an rray of entities to use to constrain the surface; valid entities are:

    - [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
    - [sketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)
  - VBA, VB.NET, C#, and C++/CLI: Not supported
  - See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.html)
[IFillSurfaceFeatureData::GetConstraintCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.html)
[IFillSurfaceFeatureData::SetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
