---
title: "EntitiesToMate Property (ISymmetricMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISymmetricMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (ISymmetricMateFeatureData)

Gets or sets the entities in this symmetry mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISymmetricMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of two similar entities: [vertexes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html), [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [axes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), [sketch lines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), [planar faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), spheres of equal radii, or cylinders of equal radii

## VBA Syntax

See [SymmetricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate.html).

## Examples

See the [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.html) examples.

## See Also

[ISymmetricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.html)
[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
