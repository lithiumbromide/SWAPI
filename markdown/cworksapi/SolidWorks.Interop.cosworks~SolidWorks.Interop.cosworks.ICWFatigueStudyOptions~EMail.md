---
title: "EMail Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "EMail"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMail.html"
---

# EMail Property (ICWFatigueStudyOptions)

Obsolete. Superseded by [ICWFatigueStudyOptions::Email2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMail2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
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

See [CWFatigueStudyOptions::EMail](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~EMail.html).

## Remarks

If this property is set to 1:

- use [ICWFatigueStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTo.html) to specify the recipient of notifications.
- use [ICWFatigueStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTimebased.html) to send email notifications during simulations.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
