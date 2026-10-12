---
title: "IGetEntitiesNeedUserId Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetEntitiesNeedUserId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEntitiesNeedUserId.html"
---

# IGetEntitiesNeedUserId Method (IMacroFeatureData)

Gets a list of faces and edges that need be assigned user IDs for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetEntitiesNeedUserId( _
   ByVal Body As Body2, _
   ByVal FaceCount As System.Integer, _
   ByRef Faces As Face2, _
   ByVal EdgeCount As System.Integer, _
   ByRef Edges As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Body As Body2
Dim FaceCount As System.Integer
Dim Faces As Face2
Dim EdgeCount As System.Integer
Dim Edges As Edge

instance.IGetEntitiesNeedUserId(Body, FaceCount, Faces, EdgeCount, Edges)
```

### C#

```csharp
void IGetEntitiesNeedUserId(
   Body2 Body,
   System.int FaceCount,
   out Face2 Faces,
   System.int EdgeCount,
   out Edge Edges
)
```

### C++/CLI

```cpp
void IGetEntitiesNeedUserId(
   Body2^ Body,
   System.int FaceCount,
   [Out] Face2^ Faces,
   System.int EdgeCount,
   [Out] Edge^ Edges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`: [Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) containing the faces and edges
- `FaceCount`: Number of faces
- `Faces`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `EdgeCount`: Number of edges
- `Edges`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMacroFeatureData::GetEntitiesNeedUserIdCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.html) to determine the size of the arrays.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEdgeIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.html)
[IMacroFeatureData::GetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.html)
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.html)
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.html)
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.html)
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.html)
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
