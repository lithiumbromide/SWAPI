---
title: "SetEntitiesToSplit Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "SetEntitiesToSplit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.html"
---

# SetEntitiesToSplit Method (IPartingLineFeatureData)

Sets the entities to use to split a face and add edges to the parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntitiesToSplit( _
   ByVal PVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim PVar As System.Object

instance.SetEntitiesToSplit(PVar)
```

### C#

```csharp
void SetEntitiesToSplit(
   System.object PVar
)
```

### C++/CLI

```cpp
void SetEntitiesToSplit(
   System.Object^ PVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PVar`: Array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) or [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [PartingLineFeatureData::SetEntitiesToSplit](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~SetEntitiesToSplit.html).

## Remarks

If sketch segments and vertices are specified, then a pair of vertices appear together; for example, segment1, vtx11, vtx12, segment2, vtx21, vtx22, vtx31, vtx32, and so on.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::ISetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.html)
[IPartingLineFeatureData::GetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.html)
[IPartingLineFeatureData::GetEntitiesToSplitCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.html)
[IPartingLineFeatureData::IGetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetEntitiesToSplit.html)
[IPartingLineFeatureData::SplitFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.html)
[IPartingLineFeatureData::SplitFacesOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
