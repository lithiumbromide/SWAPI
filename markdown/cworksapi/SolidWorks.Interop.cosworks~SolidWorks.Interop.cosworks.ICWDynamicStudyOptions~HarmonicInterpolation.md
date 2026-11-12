---
title: "HarmonicInterpolation Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "HarmonicInterpolation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicInterpolation.html"
---

# HarmonicInterpolation Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetHarmonicInterpolation2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicInterpolation2.html) and [ICWDynamicStudyOptions::SetHarmonicInterpolation2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicInterpolation2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property HarmonicInterpolation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.HarmonicInterpolation = value

value = instance.HarmonicInterpolation
```

### C#

```csharp
System.int HarmonicInterpolation {get; set;}
```

### C++/CLI

```cpp
property System.int HarmonicInterpolation {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Interpolation method as defined in [swsInterpolationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsInterpolationType_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::HarmonicInterpolation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~HarmonicInterpolation.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::HarmonicBandwidth Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicBandwidth.html)
[ICWDynamicStudyOptions::HarmonicFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUnits.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::HarmonicNoOfPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicNoOfPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
