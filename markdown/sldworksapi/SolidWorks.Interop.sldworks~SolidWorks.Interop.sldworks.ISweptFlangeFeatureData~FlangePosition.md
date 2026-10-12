---
title: "FlangePosition Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "FlangePosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlangePosition.html"
---

# FlangePosition Property (ISweptFlangeFeatureData)

Gets or sets the flange position of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlangePosition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Integer

instance.FlangePosition = value

value = instance.FlangePosition
```

### C#

```csharp
System.int FlangePosition {get; set;}
```

### C++/CLI

```cpp
property System.int FlangePosition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flange position as defined by [swSweptFlangePostionTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangePositionTypes_e.html)

## VBA Syntax

See [SweptFlangeFeatureData::FlangePosition](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~FlangePosition.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
