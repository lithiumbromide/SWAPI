---
title: "AddEdges Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "AddEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AddEdges.html"
---

# AddEdges Method (IEdgeFlangeFeatureData)

Adds edges to this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddEdges( _
   ByVal EdgeArray As System.Object, _
   ByVal SketchArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim EdgeArray As System.Object
Dim SketchArray As System.Object
Dim value As System.Integer

value = instance.AddEdges(EdgeArray, SketchArray)
```

### C#

```csharp
System.int AddEdges(
   System.object EdgeArray,
   System.object SketchArray
)
```

### C++/CLI

```cpp
System.int AddEdges(
   System.Object^ EdgeArray,
   System.Object^ SketchArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeArray`: Array of [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)s associated with SketchArray
- `SketchArray`: Array of [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)es associated with EdgeArray

### Return Value

Error code as defined by [swEdgeFlangeError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeFlangeError_e.html)

## VBA Syntax

See [EdgeFlangeFeatureData::AddEdges](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~AddEdges.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

Before calling this method, call [IModelDoc2::InsertSketchForEdgeFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange.html) to associate the sketches with the edges.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.html)
[IEdgeFlangeFeatureData::RemoveEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~RemoveEdges.html)
[IEdgeFlangeFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.html)
[IEdgeFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.html)

## Availability

SOLIDWORKS 2012 SP02, Revision Number 20.2
