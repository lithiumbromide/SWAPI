---
title: "ISetEntitiesToSplit Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "ISetEntitiesToSplit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.html"
---

# ISetEntitiesToSplit Method (IPartingLineFeatureData)

Sets the entities to use to split a face and add edges to the parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEntitiesToSplit( _
   ByVal Count As System.Integer, _
   ByRef EntIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim EntIn As System.Object

instance.ISetEntitiesToSplit(Count, EntIn)
```

### C#

```csharp
void ISetEntitiesToSplit(
   System.int Count,
   ref System.object EntIn
)
```

### C++/CLI

```cpp
void ISetEntitiesToSplit(
   System.int Count,
   System.Object^% EntIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities
- `EntIn`: - in-process, unmanaged C++: Pointer to an array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) or [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

## Remarks

If sketch segments and vertices are specified, then a pair of vertices appear together; for example, segment1, vtx11, vtx12, segment2, vtx21, vtx22, vtx31, vtx32, and so on.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::SetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.html)
[IPartingLineFeatureData::GetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.html)
[IPartingLineFeatureData::GetEntitiesToSplitCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.html)
[IPartingLineFeatureData::IGetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetEntitiesToSplit.html)
[IPartingLineFeatureData::SplitFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.html)
[IPartingLineFeatureData::SplitFacesOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
