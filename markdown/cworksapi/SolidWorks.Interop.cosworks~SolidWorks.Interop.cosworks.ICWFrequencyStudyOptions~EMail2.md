---
title: "EMail2 Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "EMail2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMail2.html"
---

# EMail2 Property (ICWFrequencyStudyOptions)

Gets or sets whether to email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMail2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

-1 or true to email notifications during simulations, 0 or false to not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1:

- use [ICWFrequencyStudyOptions::EMailTo](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTo.html) to specify the recipient of notifications.
- use [ICWFrequencyStudyOptions::EMailTimebased2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTimebased2.html) to send email notifications during simulations.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
