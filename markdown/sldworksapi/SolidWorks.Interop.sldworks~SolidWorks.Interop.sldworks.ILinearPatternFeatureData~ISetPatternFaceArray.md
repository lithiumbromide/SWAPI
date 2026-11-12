---
title: "ISetPatternFaceArray Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "ISetPatternFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternFaceArray.html"
---

# ISetPatternFaceArray Method (ILinearPatternFeatureData)

Sets the list of patterned faces for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPatternFaceArray( _
   ByVal FaceCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim FaceCount As System.Integer
Dim ArrayDataIn As System.Object

instance.ISetPatternFaceArray(FaceCount, ArrayDataIn)
```

### C#

```csharp
void ISetPatternFaceArray(
   System.int FaceCount,
   ref System.object ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetPatternFaceArray(
   System.int FaceCount,
   System.Object^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of faces of size FaceCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetPatternFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetPatternFaceCount.html)
[ILinearPatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternFaceArray.html)
[ILinearPatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFaceArray.html)
[ILinearPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
