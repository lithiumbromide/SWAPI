---
title: "EMailTimebased Property (ICWDropTestStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestStudyOptions"
member: "EMailTimebased"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailTimebased.html"
---

# EMailTimebased Property (ICWDropTestStudyOptions)

Obsolete. Superseded by [ICWDropTestStudyOptions::EmailTimebased2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailTimebased2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestStudyOptions
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

See [CWDropTestStudyOptions::EMailTimebased](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestStudyOptions~EMailTimebased.html).

## Remarks

This property is valid only if [ICWDropTestStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMail.html) is set to 1.

If this property is set to 1, use [ICWDropTestStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailInterval.html) and [ICWDropTestStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
[ICWDropTestStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
