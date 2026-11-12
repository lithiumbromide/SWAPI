---
title: "UseLowerBoundFrequency2 Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "UseLowerBoundFrequency2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseLowerBoundFrequency2.html"
---

# UseLowerBoundFrequency2 Property (ICWFrequencyStudyOptions)

Gets or sets whether to calculate frequencies closest to a specified frequency in this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLowerBoundFrequency2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Boolean

instance.UseLowerBoundFrequency2 = value

value = instance.UseLowerBoundFrequency2
```

### C#

```csharp
System.bool UseLowerBoundFrequency2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseLowerBoundFrequency2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to calculate frequencies closest to a specified frequency, 0 or false to not

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::Options](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~Options.html) is set to [swsFrequencyStudyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If you set this property to -1, use [ICWFrequencyStudyOptions::LowerBoundFrequency](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~LowerBoundFrequency.html) to specify the frequency shift.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
