---
title: "EMailTimebased2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "EMailTimebased2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailTimebased2.html"
---

# EMailTimebased2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to send email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.EMailTimebased2 = value

value = instance.EMailTimebased2
```

### C#

```csharp
System.bool EMailTimebased2 {get; set;}
```

### C++/CLI

```cpp
property System.bool EMailTimebased2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to send email notifications during simulations, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::EMailTimebased2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~EMailTimebased2.html).

## Remarks

This property is valid only if [ICWNonLinearStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMail.html) is set to -1 or true.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1 or true, use [ICWNonLinearStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailInterval.html) and [ICWNonLinearStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
