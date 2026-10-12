---
title: "GetEntitiesNeedUserId Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetEntitiesNeedUserId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.html"
---

# GetEntitiesNeedUserId Method (IMacroFeatureData)

Gets a list of faces and edges that need be assigned user IDs for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetEntitiesNeedUserId( _
   ByVal Body As System.Object, _
   ByRef Faces As System.Object, _
   ByRef Edges As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Body As System.Object
Dim Faces As System.Object
Dim Edges As System.Object

instance.GetEntitiesNeedUserId(Body, Faces, Edges)
```

### C#

```csharp
void GetEntitiesNeedUserId(
   System.object Body,
   out System.object Faces,
   out System.object Edges
)
```

### C++/CLI

```cpp
void GetEntitiesNeedUserId(
   System.Object^ Body,
   [Out] System.Object^ Faces,
   [Out] System.Object^ Edges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`: [Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) containing the faces and edges
- `Faces`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `Edges`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [MacroFeatureData::GetEntitiesNeedUserId](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetEntitiesNeedUserId.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEdgeIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.html)
[IMacroFeatureData::GetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.html)
[IMacroFeatureData::GetEntitiesNeedUserIdCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.html)
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.html)
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.html)
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.html)
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
