---
title: "MateAlignment Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "MateAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~MateAlignment.html"
---

# MateAlignment Property (IAngleMateFeatureData)

Gets or sets the alignment of this angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateAlignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
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

See [AngleMateFeatureData::MateAlignment](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~MateAlignment.html).

## Examples

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html) examples.

## Remarks

If this property is set to swMateAlign_e:

- swMateAlignALIGNED, then vectors normal to the selected entities point in the same direction.
- swMateAlignANTI_ALIGNED, then vectors normal to the selected entities point in opposite directions.

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
