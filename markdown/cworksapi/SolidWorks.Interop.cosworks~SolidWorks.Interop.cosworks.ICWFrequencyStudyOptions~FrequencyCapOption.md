---
title: "FrequencyCapOption Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "FrequencyCapOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FrequencyCapOption.html"
---

# FrequencyCapOption Property (ICWFrequencyStudyOptions)

Gets or sets the frequency cap for this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrequencyCapOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.FrequencyCapOption = value

value = instance.FrequencyCapOption
```

### C#

```csharp
System.int FrequencyCapOption {get; set;}
```

### C++/CLI

```cpp
property System.int FrequencyCapOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Frequency cap option as defined by [swsFrequencyCapOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyCapOption_e.html)

## VBA Syntax

See [CWFrequencyStudyOptions::FrequencyCapOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~FrequencyCapOption.html).

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::CheckDecouple](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckDecouple.html) is set to true.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
