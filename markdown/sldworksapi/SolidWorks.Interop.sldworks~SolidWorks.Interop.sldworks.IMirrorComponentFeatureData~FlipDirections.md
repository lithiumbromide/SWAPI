---
title: "FlipDirections Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "FlipDirections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~FlipDirections.html"
---

# FlipDirections Property (IMirrorComponentFeatureData)

Gets or sets whether to reverse the direction of alignment for selected alignment references.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDirections As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.FlipDirections = value

value = instance.FlipDirections
```

### C#

```csharp
System.object FlipDirections {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FlipDirections {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of Boolean values; true to flip alignment directions, false to not

## VBA Syntax

See [MirrorComponentFeatureData::FlipDirections](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~FlipDirections.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if [IMirrorComponentFeatureData::AlignmentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.html) is not Nothing or null.

If this property is not explicitly set, it defaults to false.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
