---
title: "Classification Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "Classification"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~Classification.html"
---

# Classification Property (CharacteristicsData)

Gets and sets the classification of defects for this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Classification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
Dim value As System.Integer

instance.Classification = value

value = instance.Classification
```

### C#

```csharp
System.int Classification {get; set;}
```

### C++/CLI

```cpp
property System.int Classification {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Classification of defects as defined by [swiCharacteristicClassification_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicClassification_e.html)

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
