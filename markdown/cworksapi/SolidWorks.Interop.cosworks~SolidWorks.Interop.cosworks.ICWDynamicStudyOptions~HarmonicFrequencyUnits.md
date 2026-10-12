---
title: "HarmonicFrequencyUnits Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "HarmonicFrequencyUnits"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUnits.html"
---

# HarmonicFrequencyUnits Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetHarmonicFrequencyUnits2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUnits2.html) and [ICWDynamicStudyOptions::SetHarmonicFrequencyUnits2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUnits2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property HarmonicFrequencyUnits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.HarmonicFrequencyUnits = value

value = instance.HarmonicFrequencyUnits
```

### C#

```csharp
System.int HarmonicFrequencyUnits {get; set;}
```

### C++/CLI

```cpp
property System.int HarmonicFrequencyUnits {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined by [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::HarmonicFrequencyUnits](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~HarmonicFrequencyUnits.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::HarmonicBandwidth Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicBandwidth.html)
[ICWDynamicStudyOptions::HarmonicFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::HarmonicInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicInterpolation.html)
[ICWDynamicStudyOptions::HarmonicNoOfPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicNoOfPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
