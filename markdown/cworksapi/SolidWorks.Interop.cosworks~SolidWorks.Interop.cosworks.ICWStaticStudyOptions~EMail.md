---
title: "EMail Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "EMail"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMail.html"
---

# EMail Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::EMail2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMail2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::EMail](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~EMail.html).

## Remarks

If this property is set to 1:

- use [ICWStaticStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTo.html) to specify the recipient of notifications.
- use [ICWStaticStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTimebased.html) to send email notifications during simulations.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
