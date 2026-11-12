---
title: "EMailTimebased2 Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "EMailTimebased2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailTimebased2.html"
---

# EMailTimebased2 Property (ICWFrequencyStudyOptions)

Gets or sets whether to send time-based email notifications during simulations.

## Syntax

### Visual Basic (Declaration)

```vb
Property EMailTimebased2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

This property is valid only if [ICWFrequencyStudyOptions::EMail](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMail.html) is set to 1.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1, use [ICWFrequencyStudyOptions::EMailInterval](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailInterval.html) and [ICWFrequencyStudyOptions::EMailIntervalUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~EMailIntervalUnit.html) to specify the time interval for sending email notifications during simulations.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
