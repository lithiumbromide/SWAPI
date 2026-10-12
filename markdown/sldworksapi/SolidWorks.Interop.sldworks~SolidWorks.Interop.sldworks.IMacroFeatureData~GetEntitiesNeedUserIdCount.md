---
title: "GetEntitiesNeedUserIdCount Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetEntitiesNeedUserIdCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.html"
---

# GetEntitiesNeedUserIdCount Method (IMacroFeatureData)

Gets the number of faces and edges that need to be assigned user IDs for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetEntitiesNeedUserIdCount( _
   ByVal Body As Body2, _
   ByRef FaceCount As System.Integer, _
   ByRef EdgeCount As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Body As Body2
Dim FaceCount As System.Integer
Dim EdgeCount As System.Integer

instance.GetEntitiesNeedUserIdCount(Body, FaceCount, EdgeCount)
```

### C#

```csharp
void GetEntitiesNeedUserIdCount(
   Body2 Body,
   out System.int FaceCount,
   out System.int EdgeCount
)
```

### C++/CLI

```cpp
void GetEntitiesNeedUserIdCount(
   Body2^ Body,
   [Out] System.int FaceCount,
   [Out] System.int EdgeCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`: [Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `FaceCount`: Number of faces
- `EdgeCount`: Number of edges

## VBA Syntax

See [MacroFeatureData::GetEntitiesNeedUserIdCount](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetEntitiesNeedUserIdCount.html).

## Remarks

Call this method before calling [IMacroFeatureData::IGetEntitiesNeedUserId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetEntitiesNeedUserId.html) to determine the size of the array for that method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.html)
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.html)
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.html)
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.html)
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
