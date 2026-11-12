---
title: "ISetFaceArray Method (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "ISetFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray.html"
---

# ISetFaceArray Method (IProjectionCurveFeatureData)

Sets the target faces for the projected curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaceArray( _
   ByVal FaceCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim FaceCount As System.Integer
Dim ArrayDataIn As System.Object

instance.ISetFaceArray(FaceCount, ArrayDataIn)
```

### C#

```csharp
void ISetFaceArray(
   System.int FaceCount,
   ref System.object ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetFaceArray(
   System.int FaceCount,
   System.Object^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of target faces
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of target faces of size FaceCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)
[IProjectionCurveFeatureData::GetFaceArrayCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~GetFaceArrayCount.html)
[IProjectionCurveFeatureData::IGetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~IGetFaceArray.html)
[IProjectionCurveFeatureData::FaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
