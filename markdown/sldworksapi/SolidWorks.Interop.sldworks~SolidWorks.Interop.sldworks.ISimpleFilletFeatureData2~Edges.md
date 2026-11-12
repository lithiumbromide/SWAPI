---
title: "Edges Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "Edges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Edges.html"
---

# Edges Property (ISimpleFilletFeatureData2)

Gets or sets the edges for this simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property Edges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Object

instance.Edges = value

value = instance.Edges
```

### C#

```csharp
System.object Edges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Edges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SimpleFilletFeatureData2::Edges](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~Edges.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetEdgeCount.html)
[ISimpleFilletFeatureData2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetEdges.html)
[ISimpleFilletFeatureData2::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetEdges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
