---
title: "GetEdgeUserId Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetEdgeUserId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.html"
---

# GetEdgeUserId Method (IMacroFeatureData)

Gets the user-defined IDs for the specified edge for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeUserId( _
   ByVal Edge As Edge, _
   ByRef Id1 As System.Integer, _
   ByRef Id2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Edge As Edge
Dim Id1 As System.Integer
Dim Id2 As System.Integer
Dim value As System.Boolean

value = instance.GetEdgeUserId(Edge, Id1, Id2)
```

### C#

```csharp
System.bool GetEdgeUserId(
   Edge Edge,
   out System.int Id1,
   out System.int Id2
)
```

### C++/CLI

```cpp
System.bool GetEdgeUserId(
   Edge^ Edge,
   [Out] System.int Id1,
   [Out] System.int Id2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Edge`: [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `Id1`: First ID
- `Id2`: Second ID

### Return Value

True if the IDs are valid, false if not

## VBA Syntax

See [MacroFeatureData::GetEdgeUserId](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetEdgeUserId.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEdgeIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.html)
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.html)
[IMacroFeatureData::GetEntitiesNeedUserIdCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.html)
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.html)
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.html)
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.html)
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
