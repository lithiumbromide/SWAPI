---
title: "Vertex Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "Vertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Vertex.html"
---

# Vertex Property (IChamferFeatureData2)

Gets or sets the vertex to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Property Vertex As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Object

instance.Vertex = value

value = instance.Vertex
```

### C#

```csharp
System.object Vertex {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Vertex {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Chamfered vertex

## VBA Syntax

See [ChamferFeatureData2::Vertex](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~Vertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IVertex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
