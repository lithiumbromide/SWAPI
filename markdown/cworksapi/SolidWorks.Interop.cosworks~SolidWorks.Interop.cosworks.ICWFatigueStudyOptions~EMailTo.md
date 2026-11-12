---
title: "EMailTo Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "EMailTo"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTo.html"
---

# EMailTo Property (ICWFatigueStudyOptions)

Gets or sets the recipient of email notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTo As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.String

instance.EMailTo = value

value = instance.EMailTo
```

### C#

```csharp
System.string EMailTo {get; set;}
```

### C++/CLI

```cpp
property System.String^ EMailTo {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Email address

## VBA Syntax

See [CWFatigueStudyOptions::EMailTo](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~EMailTo.html).

## Remarks

This property is valid only if [ICWFatigueStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMail.html) is set to 1.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
