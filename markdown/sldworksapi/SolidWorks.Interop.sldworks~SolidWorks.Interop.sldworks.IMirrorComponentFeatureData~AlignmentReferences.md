---
title: "AlignmentReferences Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "AlignmentReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.html"
---

# AlignmentReferences Property (IMirrorComponentFeatureData)

Gets or sets the alignment references for components whose orientation axes align to them.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlignmentReferences As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.AlignmentReferences = value

value = instance.AlignmentReferences
```

### C#

```csharp
System.object AlignmentReferences {get; set;}
```

### C++/CLI

```cpp
property System.Object^ AlignmentReferences {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html) (linear)

## VBA Syntax

See [MirrorComponentFeatureData::AlignmentReferences](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~AlignmentReferences.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if [IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.html) is not null or Nothing.

There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection. If this array contains fewer elements than IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection, then the feature will fail to be created.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)
[IMirrorComponentFeatureData::FlipDirections Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~FlipDirections.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
