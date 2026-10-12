---
title: "PlaneReferences Property (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "PlaneReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.html"
---

# PlaneReferences Property (ISlicingData)

Sets the reference entities of the first slicing plane.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property PlaneReferences As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData

instance.PlaneReferences = value
```

### C#

```csharp
System.object PlaneReferences {set;}
```

### C++/CLI

```cpp
property System.Object^ PlaneReferences {
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of reference entities (see **Remarks**)

## VBA Syntax

See [SlicingData::PlaneReferences](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~PlaneReferences.html).

## Remarks

Use this property to specify either:

- a planar entity (e.g., [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)) to produce a linear pattern of parallel slices

- or -

- a linear entity (e.g., [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)) and a vertex ([IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html), [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)) to produce a radial pattern of slices whose axis is the linear entity.

Use [ISlicingData::NumberOfPlanes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~NumberOfPlanes.html) to specify the number of slices and [ISlicingData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~Offset.html) to specify the linear or radial spacing of the slices.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
