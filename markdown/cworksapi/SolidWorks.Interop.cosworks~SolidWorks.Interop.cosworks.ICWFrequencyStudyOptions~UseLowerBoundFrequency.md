---
title: "UseLowerBoundFrequency Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "UseLowerBoundFrequency"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency.html"
---

# UseLowerBoundFrequency Property (ICWFrequencyStudyOptions)

Obsolete. Superseded by [ICWFrequencyStudyOptions::UseLowerBoundFrequency2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLowerBoundFrequency As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.UseLowerBoundFrequency = value

value = instance.UseLowerBoundFrequency
```

### C#

```csharp
System.int UseLowerBoundFrequency {get; set;}
```

### C++/CLI

```cpp
property System.int UseLowerBoundFrequency {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to calculate frequencies closest to a specified frequency, 0 to not

## VBA Syntax

See [CWFrequencyStudyOptions::UseLowerBoundFrequency](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~UseLowerBoundFrequency.html).

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::Options](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html) is set to [swsFrequencyStudyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies.

If you set this property to 1, use [ICWFrequencyStudyOptions::LowerBoundFrequency](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~LowerBoundFrequency.html) to specify the frequency shift.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::UpperBoundFrequency Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UpperBoundFrequency.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
