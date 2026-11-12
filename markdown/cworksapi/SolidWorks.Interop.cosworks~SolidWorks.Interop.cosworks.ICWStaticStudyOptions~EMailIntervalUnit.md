---
title: "EMailIntervalUnit Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "EMailIntervalUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailIntervalUnit.html"
---

# EMailIntervalUnit Property (ICWStaticStudyOptions)

Gets or sets the units of time for [ICWStaticStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailInterval.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailIntervalUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::EMailIntervalUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~EMailIntervalUnit.html).

## Remarks

This property is valid only if:

- [ICWStaticStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTimebased.html) is set to 1,

- and -

- [ICWStaticStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMail.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
