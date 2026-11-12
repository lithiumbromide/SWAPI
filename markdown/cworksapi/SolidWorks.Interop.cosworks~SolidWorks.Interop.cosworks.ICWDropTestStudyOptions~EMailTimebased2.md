---
title: "EMailTimebased2 Property (ICWDropTestStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestStudyOptions"
member: "EMailTimebased2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailTimebased2.html"
---

# EMailTimebased2 Property (ICWDropTestStudyOptions)

Gets or sets whether to email notifications during simulations are time based.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestStudyOptions
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

-1 or true if email notifications during simulations are time based, 0 or false if not

## Remarks

This property is valid only if [ICWDropTestStudyOptions::EMail2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMail2.html) is set to -1.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1, use [ICWDropTestStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailInterval.html) and [ICWDropTestStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
[ICWDropTestStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
