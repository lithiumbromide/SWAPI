---
title: "ProbingOption Property (ICWResultsProbeManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResultsProbeManager"
member: "ProbingOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager~ProbingOption.html"
---

# ProbingOption Property (ICWResultsProbeManager)

Gets or sets the option for this results probe.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProbingOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResultsProbeManager
Dim value As System.Integer

instance.ProbingOption = value

value = instance.ProbingOption
```

### C#

```csharp
System.int ProbingOption {get; set;}
```

### C++/CLI

```cpp
property System.int ProbingOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Option as defined in [swsProbePostResultOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultOption_e.html)

## VBA Syntax

See [CWResultsProbeManager::ProbingOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResultsProbeManager~ProbingOption.html).

## Examples

See the [ICWResultsProbeManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html) examples.

## See Also

[ICWResultsProbeManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)
[ICWResultsProbeManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
