---
title: "EMailTo Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "EMailTo"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~EMailTo.html"
---

# EMailTo Property (ICWThermalStudyOptions)

Gets or sets the recipient of email notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTo As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
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

See [CWThermalStudyOptions::EMailTo](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~EMailTo.html).

## Remarks

This property is valid only if [ICWThermalStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~EMail.html) is set to 1.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
