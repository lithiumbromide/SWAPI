---
title: "EMailTo Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "EMailTo"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailTo.html"
---

# EMailTo Property (ICWDynamicStudyOptions)

Gets or sets the recipient of email notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTo As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
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

See [CWDynamicStudyOptions::EMailTo](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~EMailTo.html).

## Remarks

This property is valid only if [ICWDynamicStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~EMailTo.html) is set to 1.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
