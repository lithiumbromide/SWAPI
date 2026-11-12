---
title: "EMailTimebased Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "EMailTimebased"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailTimebased.html"
---

# EMailTimebased Property (ICWBucklingStudyOptions)

Obsolete. Superseded by [ICWBucklingStudyOptions::EmailTimebased2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailTimebased2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

1 if time based, 0 if not

## VBA Syntax

See [CWBucklingStudyOptions::EMailTimebased](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~EMailTimebased.html).

## Remarks

This property is valid only if [ICWBucklingStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMail.html) is set to 1.

If this property is set to 1, use [ICWBucklingStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailInterval.html) and [ICWBucklingStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
