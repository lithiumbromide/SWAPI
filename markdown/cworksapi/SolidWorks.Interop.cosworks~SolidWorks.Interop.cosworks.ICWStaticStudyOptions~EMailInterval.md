---
title: "EMailInterval Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "EMailInterval"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailInterval.html"
---

# EMailInterval Property (ICWStaticStudyOptions)

Gets or sets the time interval for sending email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailInterval As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::EMailInterval](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~EMailInterval.html).

## Remarks

This property is:

- set in units specified by [ICWStaticStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailIntervalUnit.html).
- valid only if [ICWStaticStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTimebased.html) is set to 1, and [ICWStaticStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMail.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
