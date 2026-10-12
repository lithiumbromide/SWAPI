---
title: "DiameterType Property (IRackPinionMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRackPinionMateFeatureData"
member: "DiameterType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterType.html"
---

# DiameterType Property (IRackPinionMateFeatureData)

Gets or sets the type of diameter to set.

## Syntax

### Visual Basic (Declaration)

```vb
Property DiameterType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRackPinionMateFeatureData
Dim value As System.Integer

instance.DiameterType = value

value = instance.DiameterType
```

### C#

```csharp
System.int DiameterType {get; set;}
```

### C++/CLI

```cpp
property System.int DiameterType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of diameter to set as defined in [swRackPinionMateDistanceOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateDistanceOptions_e.html)

## VBA Syntax

See [RackPinionMateFeatureData::DiameterType](ms-its:sldworksapivb6.chm::/sldworks~RackPinionMateFeatureData~DiameterType.html).

## Examples

See the [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html) example.

## Remarks

For each full rotation of the pinion, the rack translates a distance = (pi * pinion pitch diameter). Use this property to set either the pinion pitch diameter or the rack translation distance per pinion revolution.

If this property is set to swRackPinionMateDistanceOptions_e:

- swPinionPitchDiameter, then set [IRackPinionMateFeatureData::DiameterVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterVal.html) with the pinion pitch diameter.
- swRackTravelPerRevolution, then set IRackPinionMateFeatureData::DiameterVal with the rack translation distance per revolution of the pinion.

## See Also

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html)
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
