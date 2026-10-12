---
title: "GetFaceArrayCount Method (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "GetFaceArrayCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~GetFaceArrayCount.html"
---

# GetFaceArrayCount Method (IProjectionCurveFeatureData)

Gets the number of target faces for this projected curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceArrayCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim value As System.Integer

value = instance.GetFaceArrayCount()
```

### C#

```csharp
System.int GetFaceArrayCount()
```

### C++/CLI

```cpp
System.int GetFaceArrayCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces for this projected curve

## VBA Syntax

See [ProjectionCurveFeatureData::GetFaceArrayCount](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData~GetFaceArrayCount.html).

## Remarks

Call this method before calling [IProjectionCurveFeatureData::IGetFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionCurveFeatureData~IGetFaceArray.html).

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)
[IProjectionCurveFeatureData::ISetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray.html)
[IProjectionCurveFeatureData::FaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
