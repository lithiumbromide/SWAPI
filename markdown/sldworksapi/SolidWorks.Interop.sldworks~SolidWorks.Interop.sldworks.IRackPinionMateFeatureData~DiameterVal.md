---
title: "DiameterVal Property (IRackPinionMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRackPinionMateFeatureData"
member: "DiameterVal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterVal.html"
---

# DiameterVal Property (IRackPinionMateFeatureData)

Gets or sets either the pinion pitch diameter or the rack translation distance per pinion revolution.

## Syntax

### Visual Basic (Declaration)

```vb
Property DiameterVal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRackPinionMateFeatureData
Dim value As System.Double

instance.DiameterVal = value

value = instance.DiameterVal
```

### C#

```csharp
System.double DiameterVal {get; set;}
```

### C++/CLI

```cpp
property System.double DiameterVal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pinion pitch diameter or rack translation distance per pinion revolution (see **Remarks**)

## VBA Syntax

See [RackPinionMateFeatureData::DiameterVal](ms-its:sldworksapivb6.chm::/sldworks~RackPinionMateFeatureData~DiameterVal.html).

## Examples

See the [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html) example.

## Remarks

For each full rotation of the pinion, the rack translates a distance = (pi * pinion pitch diameter).

If [IRackPinionMateFeatureData::DiameterType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterType.html) is set to [swRackPinionMateDistanceOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateDistanceOptions_e.html):

- swPinionPitchDiameter, use this property to specify the pinion pitch diameter.
- swRackTravelPerRevolution, use this property to specify the rack translation distance per revolution of the pinion.

## See Also

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html)
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
