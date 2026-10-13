---
title: "SubType Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "SubType"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~SubType.html"
---

# SubType Property (CharacteristicsData)

Gets the sub-type of this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SubType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
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

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
