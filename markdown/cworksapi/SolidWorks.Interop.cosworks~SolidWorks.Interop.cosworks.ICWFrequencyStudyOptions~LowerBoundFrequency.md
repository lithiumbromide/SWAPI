---
title: "LowerBoundFrequency Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "LowerBoundFrequency"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~LowerBoundFrequency.html"
---

# LowerBoundFrequency Property (ICWFrequencyStudyOptions)

Gets or sets the frequency to which frequencies closest are calculated in this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerBoundFrequency As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.LowerBoundFrequency = value

value = instance.LowerBoundFrequency
```

### C#

```csharp
System.int LowerBoundFrequency {get; set;}
```

### C++/CLI

```cpp
property System.int LowerBoundFrequency {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Frequency value to which frequencies closest are calculated

## VBA Syntax

See [CWFrequencyStudyOptions::LowerBoundFrequency](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~LowerBoundFrequency.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::Options](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html) is set to [swsFrequencyStudyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies, and [ICWFrequencyStudyOptions::UseLowerBoundFrequency](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency.html) is set to 1.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::UpperBoundFrequency Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UpperBoundFrequency.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
