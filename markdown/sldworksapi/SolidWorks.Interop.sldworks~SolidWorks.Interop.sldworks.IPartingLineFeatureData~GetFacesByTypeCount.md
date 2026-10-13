---
title: "GetFacesByTypeCount Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "GetFacesByTypeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.html"
---

# GetFacesByTypeCount Method (IPartingLineFeatureData)

Gets the number of faces of the specified type for this parting line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesByTypeCount( _
   ByVal Type As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Type As System.Integer
Dim value As System.Integer

value = instance.GetFacesByTypeCount(Type)
```

### C#

```csharp
System.int GetFacesByTypeCount(
   System.int Type
)
```

### C++/CLI

```cpp
System.int GetFacesByTypeCount(
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of faces as defined by [swDraftAnalysisFaceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisFaceType_e.html)

### Return Value

Number of faces

## VBA Syntax

See [PartingLineFeatureData::GetFacesByTypeCount](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~GetFacesByTypeCount.html).

## Remarks

Call this method before calling [IPartingLineFeatureData::IGetFacesbyType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.html).

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::GetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
