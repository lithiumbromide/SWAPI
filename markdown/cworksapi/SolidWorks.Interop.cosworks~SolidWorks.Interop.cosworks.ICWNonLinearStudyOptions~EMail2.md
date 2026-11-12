---
title: "EMail2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "EMail2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMail2.html"
---

# EMail2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.EMail2 = value

value = instance.EMail2
```

### C#

```csharp
System.bool EMail2 {get; set;}
```

### C++/CLI

```cpp
property System.bool EMail2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to email notifications during simulations, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::EMail2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~EMail2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1 or true, use:

- [ICWNonLinearStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailTo.html) to specify the recipient of notifications.
- [ICWNonLinearStudyOptions::EMailTimebased](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailTimebased.html) to send email notifications during simulations.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
