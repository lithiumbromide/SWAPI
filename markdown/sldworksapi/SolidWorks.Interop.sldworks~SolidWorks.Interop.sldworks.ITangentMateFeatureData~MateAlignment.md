---
title: "MateAlignment Property (ITangentMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITangentMateFeatureData"
member: "MateAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData~MateAlignment.html"
---

# MateAlignment Property (ITangentMateFeatureData)

Gets or sets the mate alignment of this tangent mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateAlignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITangentMateFeatureData
Dim value As System.Integer

instance.MateAlignment = value

value = instance.MateAlignment
```

### C#

```csharp
System.int MateAlignment {get; set;}
```

### C++/CLI

```cpp
property System.int MateAlignment {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mate alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.html)

## VBA Syntax

See [TangentMateFeatureData::MateAlignment](ms-its:sldworksapivb6.chm::/sldworks~TangentMateFeatureData~MateAlignment.html).

## Examples

See the [ITangentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.html) example.

## See Also

[ITangentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.html)
[ITangentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
