---
title: "EMailInterval Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "EMailInterval"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~EMailInterval.html"
---

# EMailInterval Property (ICWThermalStudyOptions)

Gets or sets the time interval for sending email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailInterval As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
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

See [CWThermalStudyOptions::EMailInterval](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~EMailInterval.html).

## Remarks

This property is:

- set in units specified by [ICWThermalStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~EMailIntervalUnit.html).
- valid only if [ICWThermalStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~EMailTimebased.html) is set to 1, and [ICWThermalStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~EMail.html) is set to 1.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
