---
title: "ComponentOrientationsAlignToComponentOrigin Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "ComponentOrientationsAlignToComponentOrigin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin.html"
---

# ComponentOrientationsAlignToComponentOrigin Property (IMirrorComponentFeatureData)

Gets or sets the array of orientations for the components whose axes align to origins.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentOrientationsAlignToComponentOrigin As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.ComponentOrientationsAlignToComponentOrigin = value

value = instance.ComponentOrientationsAlignToComponentOrigin
```

### C#

```csharp
System.object ComponentOrientationsAlignToComponentOrigin {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ComponentOrientationsAlignToComponentOrigin {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [swMirrorComponentOrientation2_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentOrientation2_e.html) values

## VBA Syntax

See [MirrorComponentFeatureData::ComponentOrientationsAlignToComponentOrigin](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

There is a one-to-one mapping between this array and [IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.html). If there are fewer elements in this array than are in IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin, then missing orientations default to swMirrorComponentOrientation2_e.swOrientation_MirroredX_MirroredY.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
