---
title: "EMail Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "EMail"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMail.html"
---

# EMail Property (ICWFrequencyStudyOptions)

Obsolete. Superseded by [ICWFrequencyStudyOptions::Email2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMail2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.EMail = value

value = instance.EMail
```

### C#

```csharp
System.int EMail {get; set;}
```

### C++/CLI

```cpp
property System.int EMail {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to email notifications during simulations, 0 to not

## VBA Syntax

See [CWFrequencyStudyOptions::EMail](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~EMail.html).

## Remarks

If this property is set to 1:

- use [ICWFrequencyStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTo.html) to specify the recipient of notifications.
- use [ICWFrequencyStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTimebased.html) to send email notifications during simulations.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
