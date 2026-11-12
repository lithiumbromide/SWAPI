---
title: "EMailIntervalUnit Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "EMailIntervalUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailIntervalUnit.html"
---

# EMailIntervalUnit Property (ICWFatigueStudyOptions)

Gets or sets the units of time for [ICWFatigueStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailInterval.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailIntervalUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
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

See [CWFatigueStudyOptions::EMailIntervalUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~EMailIntervalUnit.html).

## Remarks

This property is valid only if:

- [ICWFatigueStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTimebased.html) is set to 1,

- and -

- [ICWFatigueStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMail.html) is set to 1.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
