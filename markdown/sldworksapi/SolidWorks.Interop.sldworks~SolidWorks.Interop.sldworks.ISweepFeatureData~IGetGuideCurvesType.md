---
title: "IGetGuideCurvesType Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "IGetGuideCurvesType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurvesType.html"
---

# IGetGuideCurvesType Method (ISweepFeatureData)

Obsolete. Gets the guide curve types for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetGuideCurvesType( _
   ByVal Count As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim Count As System.Integer
Dim value As System.Integer

value = instance.IGetGuideCurvesType(Count)
```

### C#

```csharp
System.int IGetGuideCurvesType(
   System.int Count
)
```

### C++/CLI

```cpp
System.int IGetGuideCurvesType(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of guide curves

### Return Value

- in-process, unmanaged C++: Pointer to an array of longs or integers representing the types of guide curves as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISweepFeatureData::GetGuideCurvesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISweepFeatureData~GetGuideCurvesCount.html) to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesType.html)
[ISweepFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html)
[ISweepFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetGuideCurves.html)
[ISweepFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.html)
[ISweepFeatureData::MergeSmoothFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MergeSmoothFaces.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
