---
title: "SubType Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "SubType"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~SubType.html"
---

# SubType Property (ICharacteristicsData)

Gets the sub-type of this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SubType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.Integer

value = instance.SubType
```

### C#

```csharp
System.int SubType {get;}
```

### C++/CLI

```cpp
property System.int SubType {
   System.int get();
}
```

### Property Value

Sub-type as defined by [swiCharacteristicSubType_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicSubType_e.html)

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
