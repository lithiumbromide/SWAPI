---
title: "EMail Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "EMail"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMail.html"
---

# EMail Property (ICWBucklingStudyOptions)

Obsolete. Superseded by [ICWBucklingStudyOptions::Email2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMail2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::EMail](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~EMail.html).

## Remarks

If this property is set to 1:

- use [ICWBucklingStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailTo.html) to specify the recipient of notifications.
- use [ICWBucklingStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~EMailTimebased.html) to send email notifications during simulations.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
