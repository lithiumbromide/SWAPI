---
title: "Edges Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "Edges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~Edges.html"
---

# Edges Property (IMiterFlangeFeatureData)

Gets or sets the edges for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Edges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
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

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) defining this miter flange feature

## VBA Syntax

See [MiterFlangeFeatureData::Edges](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~Edges.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~IGetEdges.html)
[IMiterFlangeFeatureData::IGetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~IGetEdgesCount.html)
[IMiterFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ISetEdges.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
