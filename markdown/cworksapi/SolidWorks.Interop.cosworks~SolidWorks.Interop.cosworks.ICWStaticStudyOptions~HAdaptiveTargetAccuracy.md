---
title: "HAdaptiveTargetAccuracy Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "HAdaptiveTargetAccuracy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveTargetAccuracy.html"
---

# HAdaptiveTargetAccuracy Property (ICWStaticStudyOptions)

Gets or sets the target accuracy of the h-adaptive mesh iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Property HAdaptiveTargetAccuracy As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Double

instance.HAdaptiveTargetAccuracy = value

value = instance.HAdaptiveTargetAccuracy
```

### C#

```csharp
System.double HAdaptiveTargetAccuracy {get; set;}
```

### C++/CLI

```cpp
property System.double HAdaptiveTargetAccuracy {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.80 <= Target accuracy <= 0.99

## VBA Syntax

See [CWStaticStudyOptions::HAdaptiveTargetAccuracy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~HAdaptiveTargetAccuracy.html).

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 1.

Target accuracy is the percent change in strain energy between two consecutive mesh iterations. Mesh iteration ends when two values differ by less than the target accuracy.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::HAdaptiveAccuracyBias Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveAccuracyBias.html)
[ICWStaticStudyOptions::HAdaptiveMaxNoIterations Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMaxNoIterations.html)
[ICWStaticStudyOptions::HAdaptiveMeshCoarsening Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMeshCoarsening.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
