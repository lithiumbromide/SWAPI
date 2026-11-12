---
title: "ISetExcludedFaces Method (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "ISetExcludedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces.html"
---

# ISetExcludedFaces Method (IFlatPatternFeatureData)

Sets the faces to exclude from this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetExcludedFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim FaceCount As System.Integer
Dim FaceArray As System.Object

instance.ISetExcludedFaces(FaceCount, FaceArray)
```

### C#

```csharp
void ISetExcludedFaces(
   System.int FaceCount,
   ref System.object FaceArray
)
```

### C++/CLI

```cpp
void ISetExcludedFaces(
   System.int FaceCount,
   System.Object^% FaceArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces to exclude
- `FaceArray`: - in-process, unmanaged C++: Pointer to an array of [IFace2s](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to exclude
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::IGetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces.html)
[IFlatPatternFeatureData::IGetExcludedFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.html)
[IFlatPatternFeatureData::ExcludedFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20
