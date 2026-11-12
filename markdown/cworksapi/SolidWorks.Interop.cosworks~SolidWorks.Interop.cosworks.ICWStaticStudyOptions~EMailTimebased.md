---
title: "EMailTimebased Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "EMailTimebased"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTimebased.html"
---

# EMailTimebased Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::EMailTimebased2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTimebased2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.EMailTimebased = value

value = instance.EMailTimebased
```

### C#

```csharp
System.int EMailTimebased {get; set;}
```

### C++/CLI

```cpp
property System.int EMailTimebased {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to send email notifications during simulations, 0 to not

## VBA Syntax

See [CWStaticStudyOptions::EMailTimebased](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~EMailTimebased.html).

## Remarks

This property is valid only if [ICWStaticStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMail.html) is set to 1.

If this property is set to 1, use [ICWStaticStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailInterval.html) and [ICWStaticStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
