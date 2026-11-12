---
title: "EMailIntervalUnit Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "EMailIntervalUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailIntervalUnit.html"
---

# EMailIntervalUnit Property (ICWDynamicStudyOptions)

Gets or sets the units of time for [ICWDynamicStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailInterval.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailIntervalUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
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

See [CWDynamicStudyOptions::EMailIntervalUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~EMailIntervalUnit.html).

## Remarks

This property is valid only if:

- [ICWDynamicStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailTimebased.html) is set to 1,

- and -

- [ICWDynamicStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMail.html) is set to 1.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
