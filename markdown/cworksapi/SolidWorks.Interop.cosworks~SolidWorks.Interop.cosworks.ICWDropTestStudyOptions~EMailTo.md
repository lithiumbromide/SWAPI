---
title: "EMailTo Property (ICWDropTestStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestStudyOptions"
member: "EMailTo"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailTo.html"
---

# EMailTo Property (ICWDropTestStudyOptions)

Gets or sets the recipient of email notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTo As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestStudyOptions
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

See [CWDropTestStudyOptions::EMailTo](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestStudyOptions~EMailTo.html).

## Remarks

This property is valid only if [ICWDropTestStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMail.html) is set to 1.

## See Also

[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
[ICWDropTestStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
