---
title: "GetPropagatingEdgesCount Method (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "GetPropagatingEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetPropagatingEdgesCount.html"
---

# GetPropagatingEdgesCount Method (ISurfaceExtendFeatureData)

Gets the propagating edges for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropagatingEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim value As System.Integer

value = instance.GetPropagatingEdgesCount()
```

### C#

```csharp
System.int GetPropagatingEdgesCount()
```

### C++/CLI

```cpp
System.int GetPropagatingEdgesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of propagating edges

## VBA Syntax

See [SurfaceExtendFeatureData::GetPropagatingEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~GetPropagatingEdgesCount.html).

## Remarks

Call this method before calling [ISurfaceExtendFeatureData::IGetPropagatingEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceExtendFeatureData~IGetPropagatingEdges.html).

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::ISetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetPropagatingEdges.html)
[ISurfaceExtendFeatureData::PropagatingEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~PropagatingEdges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
