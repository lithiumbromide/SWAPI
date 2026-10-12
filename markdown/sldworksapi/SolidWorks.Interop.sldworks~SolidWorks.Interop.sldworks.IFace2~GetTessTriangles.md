---
title: "GetTessTriangles Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.html"
---

# GetTessTriangles Method (IFace2)

Gets the triangles that make up the shaded picture tessellation for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim NoConversion As System.Boolean
Dim value As System.Object

value = instance.GetTessTriangles(NoConversion)
```

### C#

```csharp
System.object GetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.Object^ GetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`: True prohibits conversion to user units from system units, false does not

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Face2::GetTessTriangles](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTessTriangles.html).

## Examples

[Get Part Bounding Box (VBA)](Get_Part_Bounding_Box_Example_VB.htm)

## Remarks

These triangles are intended for graphics display purposes and do not represent a tessellation that can be used, for example, by a machining application. If you need the kind of accuracy associated with a machining product, traverse the body faces and extract the topology and geometry data to create your own faceting.

The format of the returned data is:

float x, y, z - First point in meters

float x, y, z - Second point in meters

float x, y, z - Third point in meters

where this data repeats itself for each of the triangles on this face.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.html)
[IFace2::GetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html)
[IFace2::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.html)
[IFace2::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.html)
[IFace2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.html)
[IFace2::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.html)
[IFace2::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.html)
[IFace2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.html)
[IFace2::IGetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.html)
[IFace2::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.html)
[IFace2::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.html)
[IFace2::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdgeSize.html)
[IFace2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.html)
[IFace2::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
