---
title: "CheckFlowPressure Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "CheckFlowPressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckFlowPressure.html"
---

# CheckFlowPressure Property (ICWFrequencyStudyOptions)

Obsolete. Superseded by [ICWFrequencyStudyOptions::CheckFlowPressure2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckFlowPressure2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.CheckFlowPressure = value

value = instance.CheckFlowPressure
```

### C#

```csharp
System.int CheckFlowPressure {get; set;}
```

### C++/CLI

```cpp
property System.int CheckFlowPressure {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to import fluid pressure loads, 0 to not

## VBA Syntax

See [CWFrequencyStudyOptions::CheckFlowPressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~CheckFlowPressure.html).

## Remarks

If this property is set to 1, use [ICWFrequencyStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FlowPressureFile.html) to set the SOLIDWORKS Flow Simulation results file.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
