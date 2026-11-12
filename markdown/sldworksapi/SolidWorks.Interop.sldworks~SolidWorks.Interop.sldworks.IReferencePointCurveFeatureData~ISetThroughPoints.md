---
title: "ISetThroughPoints Method (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "ISetThroughPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.html"
---

# ISetThroughPoints Method (IReferencePointCurveFeatureData)

Sets the points through which this curve passes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetThroughPoints( _
   ByVal Count As System.Integer, _
   ByRef Pts As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData
Dim Count As System.Integer
Dim Pts As System.Object

instance.ISetThroughPoints(Count, Pts)
```

### C#

```csharp
void ISetThroughPoints(
   System.int Count,
   ref System.object Pts
)
```

### C++/CLI

```cpp
void ISetThroughPoints(
   System.int Count,
   System.Object^% Pts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of points
- `Pts`: - in-process, unmanaged C++: Pointer to an array of points
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)
[IReferencePointCurveFeatureData::SetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints.html)
[IReferencePointCurveFeatureData::GetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints.html)
[IReferencePointCurveFeatureData::IGetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.html)
[IReferencePointCurveFeatureData::GetThroughPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
