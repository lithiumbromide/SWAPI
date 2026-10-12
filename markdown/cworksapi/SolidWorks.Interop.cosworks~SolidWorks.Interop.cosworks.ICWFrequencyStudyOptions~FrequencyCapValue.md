---
title: "FrequencyCapValue Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "FrequencyCapValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FrequencyCapValue.html"
---

# FrequencyCapValue Property (ICWFrequencyStudyOptions)

Gets or sets the frequency cap value for this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrequencyCapValue As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.FrequencyCapValue = value

value = instance.FrequencyCapValue
```

### C#

```csharp
System.int FrequencyCapValue {get; set;}
```

### C++/CLI

```cpp
property System.int FrequencyCapValue {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Frequency cap value in Hertz

## VBA Syntax

See [CWFrequencyStudyOptions::FrequencyCapValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~FrequencyCapValue.html).

## Remarks

This property is valid only when:

- [ICWFrequencyStudyOptions::CheckDecouple](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckDecouple.html) is set to true,

- and -

- [ICWFrequencyStudyOptions::FrequencyCapOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FrequencyCapOption.html) is set to [swsFrequencyCapOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyCapOption_e.html).swsFrequencyCapUserDefined.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
