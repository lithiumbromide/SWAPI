---
title: "IGetEntitiesToSplit Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "IGetEntitiesToSplit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetEntitiesToSplit.html"
---

# IGetEntitiesToSplit Method (IPartingLineFeatureData)

Gets the entities that are used to split a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntitiesToSplit( _
   ByVal Count As System.Integer, _
   ByRef TypeArr As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim TypeArr As System.Integer
Dim value As System.Object

value = instance.IGetEntitiesToSplit(Count, TypeArr)
```

### C#

```csharp
System.object IGetEntitiesToSplit(
   System.int Count,
   out System.int TypeArr
)
```

### C++/CLI

```cpp
System.Object^ IGetEntitiesToSplit(
   System.int Count,
   [Out] System.int TypeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities
- `TypeArr`: - in-process, unmanaged C++: Pointer to an array of these entities as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

    - swSelVERTICES
    - swSelSKETCHSEGS
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) or [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

The resulting edges are added to the parting line feature.

Call [IPartingLineFeatureData::GetEntitiesToSplitCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.html) before this method.

When two vertices are specified, then an edge is created between them for the parting line feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::GetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.html)
[IPartingLineFeatureData::ISetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.html)
[IPartingLineFeatureData::SetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.html)
[IPartingLineFeatureData::SplitFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.html)
[IPartingLineFeatureData::SplitFacesOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
