---
title: "AQL Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "AQL"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~AQL.html"
---

# AQL Property (ICharacteristicsData)

Gets and sets the acceptable quality level (AQL) for this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property AQL As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.AQL = value

value = instance.AQL
```

### C#

```csharp
System.string AQL {get; set;}
```

### C++/CLI

```cpp
property System.String^ AQL {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Acceptable quality level for this characteristic

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
