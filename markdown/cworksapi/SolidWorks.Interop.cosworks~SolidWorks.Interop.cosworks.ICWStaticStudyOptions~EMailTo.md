---
title: "EMailTo Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "EMailTo"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMailTo.html"
---

# EMailTo Property (ICWStaticStudyOptions)

Gets or sets the recipient of email notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTo As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::EMailTo](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~EMailTo.html).

## Remarks

This property is valid only if [ICWStaticStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~EMail.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
