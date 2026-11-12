---
title: "ReliefType Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "ReliefType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefType.html"
---

# ReliefType Property (ISweptFlangeFeatureData)

Gets or sets the bend relief type for this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Integer

instance.ReliefType = value

value = instance.ReliefType
```

### C#

```csharp
System.int ReliefType {get; set;}
```

### C++/CLI

```cpp
property System.int ReliefType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend relief type as defined by [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html)

## VBA Syntax

See [SweptFlangeFeatureData::ReliefType](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~ReliefType.html).

## Remarks

This property is valid:

- for regular swept flanges,

- and -

- for cylindrical or conical swept flanges only during creation.

The setter of this property is valid only if [ISweptFlangeFeatureData::UseDefaultBendRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultBendRelief.html) is false.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
