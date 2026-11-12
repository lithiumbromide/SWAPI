---
title: "EMailTimebased Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "EMailTimebased"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTimebased.html"
---

# EMailTimebased Property (ICWFatigueStudyOptions)

Obsolete. Superseded by [ICWFatigueStudyOptions::EmailTimebased2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTimebased2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
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

See [CWFatigueStudyOptions::EMailTimebased](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~EMailTimebased.html).

## Remarks

This property is valid only if [ICWFatigueStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMail.html) is set to 1.

If this property is set to 1, use [ICWFatigueStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailInterval.html) and [ICWFatigueStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
