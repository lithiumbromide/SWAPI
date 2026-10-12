---
title: "GetEdgeIdType Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetEdgeIdType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.html"
---

# GetEdgeIdType Method (IMacroFeatureData)

Gets the ID type of the specified edge for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeIdType( _
   ByVal Edge As Edge _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Edge As Edge
Dim value As System.Integer

value = instance.GetEdgeIdType(Edge)
```

### C#

```csharp
System.int GetEdgeIdType(
   Edge Edge
)
```

### C++/CLI

```cpp
System.int GetEdgeIdType(
   Edge^ Edge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Edge`: [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) in the feature

### Return Value

ID type as defined in [swMacroFeatureEntityIdType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureEntityIdType_e.html)

## VBA Syntax

See [MacroFeatureData::GetEdgeIdType](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetEdgeIdType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.html)
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.html)
[IMacroFeatureData::GetEntitiesNeedUserIdCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.html)
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.html)
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.html)
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.html)
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
