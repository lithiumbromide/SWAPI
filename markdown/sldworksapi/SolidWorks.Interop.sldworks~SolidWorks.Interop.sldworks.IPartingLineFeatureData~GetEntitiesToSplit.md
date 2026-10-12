---
title: "GetEntitiesToSplit Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "GetEntitiesToSplit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.html"
---

# GetEntitiesToSplit Method (IPartingLineFeatureData)

Gets the entities that are used to split a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesToSplit( _
   ByRef TypeArr As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim TypeArr As System.Object
Dim value As System.Object

value = instance.GetEntitiesToSplit(TypeArr)
```

### C#

```csharp
System.object GetEntitiesToSplit(
   out System.object TypeArr
)
```

### C++/CLI

```cpp
System.Object^ GetEntitiesToSplit(
   [Out] System.Object^ TypeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TypeArr`: Array of these entities as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

  - swSelVERTICES
  - swSelSKETCHSEGS

### Return Value

Array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) or [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [PartingLineFeatureData::GetEntitiesToSplit](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~GetEntitiesToSplit.html).

## Remarks

The resulting edges are added to the parting line feature.

When two vertices are specified, then an edge is created between them for the parting line feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::GetEntitiesToSplitCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.html)
[IPartingLineFeatureData::ISetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.html)
[IPartingLineFeatureData::SetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.html)
[IPartingLineFeatureData::SplitFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.html)
[IPartingLineFeatureData::SplitFacesOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
