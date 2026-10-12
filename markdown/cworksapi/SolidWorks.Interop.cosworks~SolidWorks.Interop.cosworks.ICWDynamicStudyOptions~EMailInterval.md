---
title: "EMailInterval Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "EMailInterval"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailInterval.html"
---

# EMailInterval Property (ICWDynamicStudyOptions)

Gets or sets the time interval for sending email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailInterval As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
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

See [CWDynamicStudyOptions::EMailInterval](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~EMailInterval.html).

## Remarks

This property is:

- set in units specified by [ICWDynamicStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailIntervalUnit.html).
- valid only if [ICWDynamicStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailTimebased.html) is set to 1, and [ICWDynamicStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMail.html) is set to 1.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
