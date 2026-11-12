---
title: "Edges Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "Edges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~Edges.html"
---

# Edges Property (IHemFeatureData)

Gets or sets the edges for this hem feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Edges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
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

See [HemFeatureData::Edges](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~Edges.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)
[IHemFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~IGetEdges.html)
[IHemFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~ISetEdges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
