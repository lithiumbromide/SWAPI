---
title: "SNCurveEstimateCutoff Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SNCurveEstimateCutoff"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateCutoff.html"
---

# SNCurveEstimateCutoff Property (ICWMaterial)

Gets or sets the cut-off point for estimating Basquin Eqation constants, B and slope (m).

## Syntax

### Visual Basic (Declaration)

```vb
Property SNCurveEstimateCutoff As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.SNCurveEstimateCutoff = value

value = instance.SNCurveEstimateCutoff
```

### C#

```csharp
System.int SNCurveEstimateCutoff {get; set;}
```

### C++/CLI

```cpp
property System.int SNCurveEstimateCutoff {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 0 or 1: no cut-off; all of the points of the S-N curve are used for fitting a straight line and calculating the Basquin Equation constants, B and m
- `n` >= `2`: cut-off point on material S-N curve; the first `n` points of the S-N curve are used by the program to fit a straight line and calculate the Basquin Equation constants, B and m

## VBA Syntax

See [CWMaterial::SNCurveEstimateCutoff](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SNCurveEstimateCutoff.html).

## Remarks

This property is valid only:

- for fatigue studies that are based on results from linear dynamic random vibration studies.
- if [ICWMaterial::SNCurveSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html) is set to [swsMaterialSNCurveSource_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSNCurveSource_e.html).swsMaterialSNCurveSourceEquation, and [ICWMaterial::SNCurveEstimateConstants](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateConstants.html) is set to 1.

See the SOLIDWORKS Help topic, **Material Dialog Box - Fatigue SN Curves Tab**, for more information about Basquin Equations.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
