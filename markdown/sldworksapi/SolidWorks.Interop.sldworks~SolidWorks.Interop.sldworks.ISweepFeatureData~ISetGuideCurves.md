---
title: "ISetGuideCurves Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "ISetGuideCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetGuideCurves.html"
---

# ISetGuideCurves Method (ISweepFeatureData)

Obsolete. Sets the guide curves for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetGuideCurves( _
   ByVal Count As System.Short, _
   ByRef PDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim Count As System.Short
Dim PDisp As System.Object

instance.ISetGuideCurves(Count, PDisp)
```

### C#

```csharp
void ISetGuideCurves(
   System.short Count,
   ref System.object PDisp
)
```

### C++/CLI

```cpp
void ISetGuideCurves(
   System.short Count,
   System.Object^% PDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of guide curves
- `PDisp`: - in-process, unmanaged C++: Pointer to an array of the [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) of the guide curves of size Count

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesCount.html)
[ISweepFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesType.html)
[ISweepFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html)
[ISweepFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurvesType.html)
[ISweepFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.html)
[ISweepFeatureData::MergeSmoothFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MergeSmoothFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
