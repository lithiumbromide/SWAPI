---
title: "GetThroughPointCount Method (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "GetThroughPointCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.html"
---

# GetThroughPointCount Method (IReferencePointCurveFeatureData)

Gets the number of points through which this curve passes.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThroughPointCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData
Dim value As System.Integer

value = instance.GetThroughPointCount()
```

### C#

```csharp
System.int GetThroughPointCount()
```

### C++/CLI

```cpp
System.int GetThroughPointCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of points

## VBA Syntax

See [ReferencePointCurveFeatureData::GetThroughPointCount](ms-its:sldworksapivb6.chm::/sldworks~ReferencePointCurveFeatureData~GetThroughPointCount.html).

## Examples

See the [IReferencePointCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html) examples.

## Remarks

Call this method before calling [IReferencePointCurveFeatureData::IGetThroughPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.html).

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)
[IReferencePointCurveFeatureData::GetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints.html)
[IReferencePointCurveFeatureData::ISetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.html)
[IReferencePointCurveFeatureData::SetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
