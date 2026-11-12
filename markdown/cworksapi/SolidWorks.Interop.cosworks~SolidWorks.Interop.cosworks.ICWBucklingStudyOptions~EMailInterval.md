---
title: "EMailInterval Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "EMailInterval"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailInterval.html"
---

# EMailInterval Property (ICWBucklingStudyOptions)

Gets or sets the time interval for sending email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailInterval As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::EMailInterval](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~EMailInterval.html).

## Remarks

This property is:

- set in units specified by [ICWBucklingStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailIntervalUnit.html).
- valid only if [ICWBucklingStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailTimebased.html) is set to 1, and [ICWBucklingStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMail.html) is set to 1.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
