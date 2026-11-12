---
title: "ISetBends Method (IFoldsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFoldsFeatureData"
member: "ISetBends"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~ISetBends.html"
---

# ISetBends Method (IFoldsFeatureData)

Sets the bend features for this fold feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBends( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFoldsFeatureData
Dim FaceCount As System.Integer
Dim FaceArray As System.Object

instance.ISetBends(FaceCount, FaceArray)
```

### C#

```csharp
void ISetBends(
   System.int FaceCount,
   ref System.object FaceArray
)
```

### C++/CLI

```cpp
void ISetBends(
   System.int FaceCount,
   System.Object^% FaceArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces describing the bends
- `FaceArray`: - in-process, unmanaged C++: Pointer to an array of bend [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) that describe the bends that belong to this folds feature

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.html)
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.html)
[IFoldsFeatureData::IGetBends Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBends.html)
[IFoldsFeatureData::IGetBendsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBendsCount.html)
[IFoldsFeatureData::Bends Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~Bends.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
