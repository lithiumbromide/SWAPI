---
title: "MirrorType Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "MirrorType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorType.html"
---

# MirrorType Property (IMirrorComponentFeatureData)

Gets or sets the mirror position.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Integer

instance.MirrorType = value

value = instance.MirrorType
```

### C#

```csharp
System.int MirrorType {get; set;}
```

### C++/CLI

```cpp
property System.int MirrorType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of mirror as defined by [swMirrorComponentMirrorType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentMirrorType_e.html)

## VBA Syntax

See [MirrorComponentFeatureData::MirrorType](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~MirrorType.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

If not explicitly set, this property defaults to swMirrorComponentMirrorType_e.swMirrorType_CenterOfBoundingBox.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
