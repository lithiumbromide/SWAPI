---
title: "EMailIntervalUnit Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "EMailIntervalUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailIntervalUnit.html"
---

# EMailIntervalUnit Property (ICWBucklingStudyOptions)

Gets or sets the units of time for [ICWBucklingStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailInterval.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailIntervalUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::EMailIntervalUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~EMailIntervalUnit.html).

## Remarks

This property is valid only if:

- [ICWBucklingStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailTimebased.html) is set to 1,

- and -

- [ICWBucklingStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMail.html) is set to 1.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
