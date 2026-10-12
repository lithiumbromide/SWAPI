---
title: "IGetThroughPoints Method (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "IGetThroughPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.html"
---

# IGetThroughPoints Method (IReferencePointCurveFeatureData)

Gets the points through which this curve passes.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetThroughPoints( _
   ByVal Count As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData
Dim Count As System.Integer
Dim Type As System.Integer
Dim value As System.Object

value = instance.IGetThroughPoints(Count, Type)
```

### C#

```csharp
System.object IGetThroughPoints(
   System.int Count,
   out System.int Type
)
```

### C++/CLI

```cpp
System.Object^ IGetThroughPoints(
   System.int Count,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of points
- `Type`: Type of entities (sketch points or vertices) as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

- in-process, unmanaged C++: Pointer to an array of points

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IReferencePointCurveFeatureData::GetThroughPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)
[IReferencePointCurveFeatureData::GetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints.html)
[IReferencePointCurveFeatureData::ISetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.html)
[IReferencePointCurveFeatureData::SetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
