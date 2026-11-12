---
title: "EMailTimebased Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "EMailTimebased"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTimebased.html"
---

# EMailTimebased Property (ICWFrequencyStudyOptions)

Obsolete. Superseded by [ICWFrequencyStudyOptions::EmailTimebased2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTimebased2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

See [CWFrequencyStudyOptions::EMailTimebased](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~EMailTimebased.html).

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMail.html) is set to 1.

If this property is set to 1, use [ICWFrequencyStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailInterval.html) and [ICWFrequencyStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
