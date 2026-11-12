---
title: "Edge Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "Edge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edge.html"
---

# Edge Property (IEdgeFlangeFeatureData)

Obsolete. Superseded by [IEdgeFlangeFeatureData::Edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~Edges.html), [IEdgeFlangeFeatureData::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.html), and [IEdgeFlangeFeatureData::ISetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Edge As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Object

instance.Edge = value

value = instance.Edge
```

### C#

```csharp
System.object Edge {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Edge {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [EdgeFlangeFeatureData::Edge](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~Edge.html).

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
