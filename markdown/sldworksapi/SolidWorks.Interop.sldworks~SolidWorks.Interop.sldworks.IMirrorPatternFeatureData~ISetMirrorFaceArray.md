---
title: "ISetMirrorFaceArray Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "ISetMirrorFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetMirrorFaceArray.html"
---

# ISetMirrorFaceArray Method (IMirrorPatternFeatureData)

Sets the faces to mirror.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetMirrorFaceArray( _
   ByVal FaceCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim FaceCount As System.Integer
Dim ArrayDataIn As System.Object

instance.ISetMirrorFaceArray(FaceCount, ArrayDataIn)
```

### C#

```csharp
void ISetMirrorFaceArray(
   System.int FaceCount,
   ref System.object ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetMirrorFaceArray(
   System.int FaceCount,
   System.Object^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size FaceCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::GetMirrorFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetMirrorFaceCount.html)
[IMirrorPatternFeatureData::IGetMirrorFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetMirrorFaceArray.html)
[IMirrorPatternFeatureData::MirrorFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~MirrorFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
