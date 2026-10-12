---
title: "EMail Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "EMail"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMail.html"
---

# EMail Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::Email2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMail2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::EMail](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~EMail.html).

## Remarks

If this property is set to 1:

- use [ICWNonLinearStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailTo.html) to specify the recipient of notifications.
- use [ICWNonLinearStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailTimebased.html) to send email notifications during simulations.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
