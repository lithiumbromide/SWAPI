---
title: "Vertex Property (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "Vertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~Vertex.html"
---

# Vertex Property (ISurfaceExtendFeatureData)

Gets and sets the vertex for the end condition of this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Vertex As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
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

End-condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SurfaceExtendFeatureData::Vertex](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~Vertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IVertex.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
