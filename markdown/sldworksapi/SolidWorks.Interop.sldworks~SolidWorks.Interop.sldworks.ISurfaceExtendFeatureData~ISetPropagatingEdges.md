---
title: "ISetPropagatingEdges Method (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "ISetPropagatingEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetPropagatingEdges.html"
---

# ISetPropagatingEdges Method (ISurfaceExtendFeatureData)

Sets the propagating edges for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPropagatingEdges( _
   ByVal Count As System.Integer, _
   ByRef EdgeArr As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim Count As System.Integer
Dim EdgeArr As Edge

instance.ISetPropagatingEdges(Count, EdgeArr)
```

### C#

```csharp
void ISetPropagatingEdges(
   System.int Count,
   ref Edge EdgeArr
)
```

### C++/CLI

```cpp
void ISetPropagatingEdges(
   System.int Count,
   Edge^% EdgeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of propagating edges
- `EdgeArr`: - in-process, unmanaged C++: Pointer to an array extended items ([faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) and [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::GetPropagatingEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetPropagatingEdgesCount.html)
[ISurfaceExtendFeatureData::IGetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IGetPropagatingEdges.html)
[ISurfaceExtendFeatureData::PropagatingEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~PropagatingEdges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
