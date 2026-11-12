---
title: "IVertex Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "IVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IVertex.html"
---

# IVertex Property (IChamferFeatureData2)

Gets or sets the vertex to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Property IVertex As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As Vertex

instance.IVertex = value

value = instance.IVertex
```

### C#

```csharp
Vertex IVertex {get; set;}
```

### C++/CLI

```cpp
property Vertex^ IVertex {
   Vertex^ get();
   void set (    Vertex^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Chamfered vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [ChamferFeatureData2::IVertex](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~IVertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Vertex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
