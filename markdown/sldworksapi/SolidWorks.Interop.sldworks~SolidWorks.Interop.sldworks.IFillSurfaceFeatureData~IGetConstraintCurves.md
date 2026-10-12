---
title: "IGetConstraintCurves Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "IGetConstraintCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetConstraintCurves.html"
---

# IGetConstraintCurves Method (IFillSurfaceFeatureData)

Gets the constraint curves for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConstraintCurves( _
   ByVal Count As System.Integer, _
   ByRef TypeArr As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim TypeArr As System.Integer
Dim value As System.Object

value = instance.IGetConstraintCurves(Count, TypeArr)
```

### C#

```csharp
System.object IGetConstraintCurves(
   System.int Count,
   out System.int TypeArr
)
```

### C++/CLI

```cpp
System.Object^ IGetConstraintCurves(
   System.int Count,
   [Out] System.int TypeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities used to constrain the surface
- `TypeArr`: - in-process, unmanaged C++: Pointer to an array of types of entities used to constrain the surface as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html); valid entities are:

    - edges (swSelEDGES)
    - sketches (swSelSKETCHES)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of entities used as constraint curves

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IFillSurfaceFeatureData::GetConstraintCurvesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.html)
[IFillSurfaceFeatureData::ISetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.html)
[IFillSurfaceFeatureData::SetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
