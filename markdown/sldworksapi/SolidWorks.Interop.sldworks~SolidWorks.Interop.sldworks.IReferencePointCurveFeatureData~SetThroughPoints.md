---
title: "SetThroughPoints Method (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "SetThroughPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints.html"
---

# SetThroughPoints Method (IReferencePointCurveFeatureData)

Sets the points through which this curve passes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetThroughPoints( _
   ByVal Pts As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData
Dim Pts As System.Object

instance.SetThroughPoints(Pts)
```

### C#

```csharp
void SetThroughPoints(
   System.object Pts
)
```

### C++/CLI

```cpp
void SetThroughPoints(
   System.Object^ Pts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Pts`: Array of points

## VBA Syntax

See [ReferencePointCurveFeatureData::SetThroughPoints](ms-its:sldworksapivb6.chm::/sldworks~ReferencePointCurveFeatureData~SetThroughPoints.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)
[IReferencePointCurveFeatureData::ISetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.html)
[IReferencePointCurveFeatureData::GetThroughPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.html)
[IReferencePointCurveFeatureData::GetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints.html)
[IReferencePointCurveFeatureData::IGetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
