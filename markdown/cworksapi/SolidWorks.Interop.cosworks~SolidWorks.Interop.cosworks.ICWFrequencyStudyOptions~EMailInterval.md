---
title: "EMailInterval Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "EMailInterval"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailInterval.html"
---

# EMailInterval Property (ICWFrequencyStudyOptions)

Gets or sets the time interval for sending email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailInterval As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.EMailInterval = value

value = instance.EMailInterval
```

### C#

```csharp
System.int EMailInterval {get; set;}
```

### C++/CLI

```cpp
property System.int EMailInterval {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Time interval

## VBA Syntax

See [CWFrequencyStudyOptions::EMailInterval](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~EMailInterval.html).

## Remarks

This property is:

- set in units specified by [ICWFrequencyStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailIntervalUnit.html).
- valid only if [ICWFrequencyStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTimebased.html) is set to 1, and [ICWFrequencyStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMail.html) is set to 1.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
