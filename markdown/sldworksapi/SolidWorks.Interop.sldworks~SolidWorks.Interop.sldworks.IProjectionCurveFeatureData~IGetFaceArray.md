---
title: "IGetFaceArray Method (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "IGetFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~IGetFaceArray.html"
---

# IGetFaceArray Method (IProjectionCurveFeatureData)

Gets a list of target faces for the projected curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaceArray( _
   ByVal FaceCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim FaceCount As System.Integer
Dim value As System.Object

value = instance.IGetFaceArray(FaceCount)
```

### C#

```csharp
System.object IGetFaceArray(
   System.int FaceCount
)
```

### C++/CLI

```cpp
System.Object^ IGetFaceArray(
   System.int FaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of target faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of target faces of size FaceCount

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IProjectionCurveFeatureData::GetFaceArrayCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionCurveFeatureData~GetFaceArrayCount.html) before calling this method to get the value of FaceCount.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)
[IProjectionCurveFeatureData::ISetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray.html)
[IProjectionCurveFeatureData::FaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
