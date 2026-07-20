---
title: "GetTessNorms Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetTessNorms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html"
---

# GetTessNorms Method (IPartDoc)

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessNorms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Object

value = instance.GetTessNorms()
```

### C#

```csharp
System.object GetTessNorms()
```

### C++/CLI

```cpp
System.Object^ GetTessNorms();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of floats (see

Remarks

)

## VBA Syntax

See

[PartDoc::GetTessNorms](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetTessNorms.html)

.

## Remarks

The total size of the data is:

[9 x sizeof(float) x (number of triangles)].

The format of the returned data is:

- floatx, y, z first point's unit normal
- floatx, y, z second point's unit normal
- floatx, y, z third point's unit normal

for the set of triangles for the part.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)

[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)

[IPartDoc::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html)

[IPartDoc::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html)

[IPartDoc::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.html)

[IPartDoc::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessNorms.html)

[IPartDoc::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriangles.html)

[IPartDoc::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdges.html)

[IPartDoc::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdgeSize.html)

[IPartDoc::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripNorms.html)

[IPartDoc::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStrips.html)

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)

[IPartDoc::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.html)
