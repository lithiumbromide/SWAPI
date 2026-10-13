---
title: "IVertex Property (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "IVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IVertex.html"
---

# IVertex Property (ISurfaceExtendFeatureData)

Gets and sets the vertex for the end condition of this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IVertex As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
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

End-condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SurfaceExtendFeatureData::IVertex](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~IVertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~Vertex.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
