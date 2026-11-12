---
title: "HarmonicFrequencyUpperLimit Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "HarmonicFrequencyUpperLimit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html"
---

# HarmonicFrequencyUpperLimit Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetHarmonicFrequencyUpperLimit2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUpperLimit2.html) and [ICWDynamicStudyOptions::SetHarmonicFrequencyLimit2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUpperLimit2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property HarmonicFrequencyUpperLimit As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.HarmonicFrequencyUpperLimit = value

value = instance.HarmonicFrequencyUpperLimit
```

### C#

```csharp
System.double HarmonicFrequencyUpperLimit {get; set;}
```

### C++/CLI

```cpp
property System.double HarmonicFrequencyUpperLimit {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Frequency upper limit

## VBA Syntax

See [CWDynamicStudyOptions::HarmonicFrequencyUpperLimit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::HarmonicBandwidth Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicBandwidth.html)
[ICWDynamicStudyOptions::HarmonicFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUnits.html)
[ICWDynamicStudyOptions::HarmonicInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicInterpolation.html)
[ICWDynamicStudyOptions::HarmonicNoOfPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicNoOfPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
