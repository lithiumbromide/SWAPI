---
title: "ConfigurationName Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "ConfigurationName"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~ConfigurationName.html"
---

# ConfigurationName Property (ICharacteristicsData)

Gets the SOLIDWORKS configuration associated with this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
}
```

### Property Value

Name of a SOLIDWORKS configuration

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
