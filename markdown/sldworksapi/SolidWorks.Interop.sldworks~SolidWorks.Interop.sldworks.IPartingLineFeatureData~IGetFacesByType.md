---
title: "IGetFacesByType Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "IGetFacesByType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.html"
---

# IGetFacesByType Method (IPartingLineFeatureData)

Gets the specified faces after performing a draft analysis of the parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacesByType( _
   ByVal Type As System.Integer, _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Type As System.Integer
Dim Count As System.Integer
Dim value As Face2

value = instance.IGetFacesByType(Type, Count)
```

### C#

```csharp
Face2 IGetFacesByType(
   System.int Type,
   System.int Count
)
```

### C++/CLI

```cpp
Face2^ IGetFacesByType(
   System.int Type,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of face as defined by [swDraftAnalysisFaceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisFaceType_e.html)
- `Count`: Number of faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IPartingLineFeatureData::GetFacesByTypeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::GetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.html)
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
