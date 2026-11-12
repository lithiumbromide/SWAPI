---
title: "GetThroughPoints Method (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "GetThroughPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints.html"
---

# GetThroughPoints Method (IReferencePointCurveFeatureData)

Gets the points through which this curve passes.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThroughPoints( _
   ByRef Type As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData
Dim Type As System.Object
Dim value As System.Object

value = instance.GetThroughPoints(Type)
```

### C#

```csharp
System.object GetThroughPoints(
   out System.object Type
)
```

### C++/CLI

```cpp
System.Object^ GetThroughPoints(
   [Out] System.Object^ Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of entities (sketch points or vertices) as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Array of points

## VBA Syntax

See [ReferencePointCurveFeatureData::GetThroughPoints](ms-its:sldworksapivb6.chm::/sldworks~ReferencePointCurveFeatureData~GetThroughPoints.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)
[IReferencePointCurveFeatureData::GetThroughPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.html)
[IReferencePointCurveFeatureData::IGetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.html)
[IReferencePointCurveFeatureData::ISetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.html)
[IReferencePointCurveFeatureData::SetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
