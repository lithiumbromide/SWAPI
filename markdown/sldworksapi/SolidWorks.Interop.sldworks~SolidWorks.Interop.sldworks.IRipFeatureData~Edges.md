---
title: "Edges Property (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "Edges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Edges.html"
---

# Edges Property (IRipFeatureData)

Gets or sets the edges for this rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Edges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
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

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [RipFeatureData::Edges](ms-its:sldworksapivb6.chm::/sldworks~RipFeatureData~Edges.html).

## Examples

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)
[IRipFeatureData::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetEdgesCount.html)
[IRipFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~IGetEdges.html)
[IRipFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~ISetEdges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
