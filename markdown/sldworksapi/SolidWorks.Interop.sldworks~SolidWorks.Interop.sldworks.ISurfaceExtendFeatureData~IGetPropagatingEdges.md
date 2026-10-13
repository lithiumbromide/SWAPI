---
title: "IGetPropagatingEdges Method (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "IGetPropagatingEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IGetPropagatingEdges.html"
---

# IGetPropagatingEdges Method (ISurfaceExtendFeatureData)

Gets the propagating edges for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPropagatingEdges( _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetPropagatingEdges(Count)
```

### C#

```csharp
Edge IGetPropagatingEdges(
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetPropagatingEdges(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of propagating edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of propagating [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISurfaceExtendFeatureData::GetPropagatingEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceExtendFeatureData~GetPropagatingEdgesCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
