---
title: "ISetPatternFaceArray Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "ISetPatternFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternFaceArray.html"
---

# ISetPatternFaceArray Method (ICircularPatternFeatureData)

Sets a list of patterned faces for this circular pattern.

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
Dim instance As ICircularPatternFeatureData
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

- `FaceCount`: Number of patterned faces
- `ArrayDataIn`: in-process, unmanaged C++: Pointer to an array of patterned [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size FaceCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::GetPatternFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternFaceCount.html)
[ICircularPatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternFaceArray.html)
[ICircularPatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternFaceArray.html)
[ICircularPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
