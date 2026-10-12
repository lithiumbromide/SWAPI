---
title: "EMailIntervalUnit Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "EMailIntervalUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailIntervalUnit.html"
---

# EMailIntervalUnit Property (ICWNonLinearStudyOptions)

Gets or sets the units of time for [ICWNonLinearStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailInterval.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailIntervalUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.EMailIntervalUnit = value

value = instance.EMailIntervalUnit
```

### C#

```csharp
System.int EMailIntervalUnit {get; set;}
```

### C++/CLI

```cpp
property System.int EMailIntervalUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Time units as defined in [swsTimeUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTimeUnits_e.html):

- swsSecond
- swsMinute
- swsHour

## VBA Syntax

See [CWNonLinearStudyOptions::EMailIntervalUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~EMailIntervalUnit.html).

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailTimebased.html) is set to 1,

- and -

- [ICWNonLinearStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMail.html) is set to 1.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
