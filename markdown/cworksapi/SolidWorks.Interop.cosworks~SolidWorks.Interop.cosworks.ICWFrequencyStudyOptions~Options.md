---
title: "Options Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "Options"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html"
---

# Options Property (ICWFrequencyStudyOptions)

Gets or sets the frequency option for this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property Options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.Options = value

value = instance.Options
```

### C#

```csharp
System.int Options {get; set;}
```

### C++/CLI

```cpp
property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Option as defined in [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html)

## VBA Syntax

See [CWFrequencyStudyOptions::Options](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~Options.html).

## Remarks

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::NoOfFrequencies Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~NoOfFrequencies.html)
[ICWFrequencyStudyOptions::UpperBoundFrequency Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UpperBoundFrequency.html)
[ICWFrequencyStudyOptions::UseLowerBoundFrequency Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
