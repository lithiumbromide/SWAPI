---
title: "NoOfFrequencies Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "NoOfFrequencies"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~NoOfFrequencies.html"
---

# NoOfFrequencies Property (ICWFrequencyStudyOptions)

Gets or sets the number of frequencies in this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoOfFrequencies As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.NoOfFrequencies = value

value = instance.NoOfFrequencies
```

### C#

```csharp
System.int NoOfFrequencies {get; set;}
```

### C++/CLI

```cpp
property System.int NoOfFrequencies {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of frequencies

## VBA Syntax

See [CWFrequencyStudyOptions::NoOfFrequencies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~NoOfFrequencies.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::Options](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html) is set to [swsFrequencyStudyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::UseLowerBoundFrequency Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency.html)
[ICWFrequencyStudyOptions::LowerBoundFrequency Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~LowerBoundFrequency.html)
[ICWFrequencyStudyOptions::UpperBoundFrequency Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UpperBoundFrequency.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
