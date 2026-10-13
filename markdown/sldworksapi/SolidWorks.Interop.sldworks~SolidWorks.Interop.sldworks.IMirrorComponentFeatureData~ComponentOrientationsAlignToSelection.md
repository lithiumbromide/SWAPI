---
title: "ComponentOrientationsAlignToSelection Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "ComponentOrientationsAlignToSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToSelection.html"
---

# ComponentOrientationsAlignToSelection Property (IMirrorComponentFeatureData)

Gets or sets the array of orientations for the components whose axes align to a selected reference.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentOrientationsAlignToSelection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.ComponentOrientationsAlignToSelection = value

value = instance.ComponentOrientationsAlignToSelection
```

### C#

```csharp
System.object ComponentOrientationsAlignToSelection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ComponentOrientationsAlignToSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [swMirrorComponentOrientation2_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentOrientation2_e.html) values

## VBA Syntax

See [MirrorComponentFeatureData::ComponentOrientationsAlignToSelection](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~ComponentOrientationsAlignToSelection.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

There is a one-to-one mapping between this array and [IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.html). If there are fewer elements in this array than are in IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection, then missing orientations default to swMirrorComponentOrientation2_e.swOrientation_MirroredX_MirroredY.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
