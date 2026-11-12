---
title: "IGetTessTriangles Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriangles.html"
---

# IGetTessTriangles Method (IPartDoc)

Gets the triangles that make up the shaded picture tessellation for this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriangles(NoConversion)
```

### C#

```csharp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`: True to prohibit conversion to user units from system units , false to do so

### Return Value

- in-process, unmanaged C++: Pointer to an array of floats (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

These triangles are intended for graphics display purposes and do not represent a tessellation that could be used, for example, by a machining application. If you need the type of accuracy associated with a machining product, it is recommended that you traverse the body faces and extract the topology and geometry data to create your own faceting.

The total size of the data is:

[ 9 x sizeof(float ) x (number of triangles) ].

The format of the data is:

- float x, y, z first point in meters
- float x, y, z second point in meters
- float x, y, z third point in meters

for the set of triangles for the part.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[IPartDoc::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html)
[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)
[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)
[IPartDoc::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html)
[IPartDoc::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html)
[IPartDoc::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.html)
[IPartDoc::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.html)
[IPartDoc::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessNorms.html)
[IPartDoc::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdges.html)
[IPartDoc::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdgeSize.html)
[IPartDoc::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripNorms.html)
[IPartDoc::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStrips.html)
[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
