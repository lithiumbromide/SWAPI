---
title: "UpperBoundFrequency Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "UpperBoundFrequency"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UpperBoundFrequency.html"
---

# UpperBoundFrequency Property (ICWFrequencyStudyOptions)

Gets or sets the upper-bound frequency for this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperBoundFrequency As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.UpperBoundFrequency = value

value = instance.UpperBoundFrequency
```

### C#

```csharp
System.int UpperBoundFrequency {get; set;}
```

### C++/CLI

```cpp
property System.int UpperBoundFrequency {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Upper-bound frequency

## VBA Syntax

See [CWFrequencyStudyOptions::UpperBoundFrequency](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~UpperBoundFrequency.html).

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::Options](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html) is set to [swsFrequencyStudyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionUseUpperBoundFrequency.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::Options Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html)
[ICWFrequencyStudyOptions::LowerBoundFrequency Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~LowerBoundFrequency.html)
[ICWFrequencyStudyOptions::UseLowerBoundFrequency Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
