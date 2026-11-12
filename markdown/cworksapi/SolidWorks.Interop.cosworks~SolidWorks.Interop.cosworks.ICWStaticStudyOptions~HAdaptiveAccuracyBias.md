---
title: "HAdaptiveAccuracyBias Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "HAdaptiveAccuracyBias"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveAccuracyBias.html"
---

# HAdaptiveAccuracyBias Property (ICWStaticStudyOptions)

Gets or sets the accuracy bias for the h-adaptive mesh iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Property HAdaptiveAccuracyBias As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Double

instance.HAdaptiveAccuracyBias = value

value = instance.HAdaptiveAccuracyBias
```

### C#

```csharp
System.double HAdaptiveAccuracyBias {get; set;}
```

### C++/CLI

```cpp
property System.double HAdaptiveAccuracyBias {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 (local) <= Accuracy bias <= 1.0 (global)

## VBA Syntax

See [CWStaticStudyOptions::HAdaptiveAccuracyBias](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~HAdaptiveAccuracyBias.html).

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 1.

When iterating the mesh, accuracy bias balances:

- achieving accurate peak stress results in areas where stress concentrations exist (local)

- and -

- achieving accurate global results (global).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::HAdaptiveMaxNoIterations Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMaxNoIterations.html)
[ICWStaticStudyOptions::HAdaptiveMeshCoarsening Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMeshCoarsening.html)
[ICWStaticStudyOptions::HAdaptiveTargetAccuracy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveTargetAccuracy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
