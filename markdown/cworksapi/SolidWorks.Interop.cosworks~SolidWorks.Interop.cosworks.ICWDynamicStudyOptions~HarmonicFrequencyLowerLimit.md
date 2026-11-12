---
title: "HarmonicFrequencyLowerLimit Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "HarmonicFrequencyLowerLimit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html"
---

# HarmonicFrequencyLowerLimit Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetHarmonicFrequencyLowerLimit2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyLowerLimit2.html) and [ICWDynamicStudyOptions::SetHarmonicFrequencyLowerLimit2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyLowerLimit2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property HarmonicFrequencyLowerLimit As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.HarmonicFrequencyLowerLimit = value

value = instance.HarmonicFrequencyLowerLimit
```

### C#

```csharp
System.double HarmonicFrequencyLowerLimit {get; set;}
```

### C++/CLI

```cpp
property System.double HarmonicFrequencyLowerLimit {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Frequency lower limit

## VBA Syntax

See [CWDynamicStudyOptions::HarmonicFrequencyLowerLimit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::HarmonicBandwidth Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicBandwidth.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUnits.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::HarmonicInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicInterpolation.html)
[ICWDynamicStudyOptions::HarmonicNoOfPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicNoOfPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
