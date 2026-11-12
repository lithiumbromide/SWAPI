---
title: "EMailTimebased2 Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "EMailTimebased2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailTimebased2.html"
---

# EMailTimebased2 Property (ICWFatigueStudyOptions)

Gets or sets whether to send email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
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

-1 or true to send time-based email notifications during simulations, 0 or false to not

## Remarks

This property is valid only if [ICWFatigueStudyOptions::EMail2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMail2.html) is set to -1.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1, use [ICWFatigueStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailInterval.html) and [ICWFatigueStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
