---
title: "Key Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "Key"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~Key.html"
---

# Key Property (CharacteristicsData)

Gets and sets whether this characteristic is a key characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Key As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
Dim value As System.Boolean

instance.Key = value

value = instance.Key
```

### C#

```csharp
System.bool Key {get; set;}
```

### C++/CLI

```cpp
property System.bool Key {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if key, false if regular

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## Remarks

Key characteristics are characteristics whose variation has a significant impact on the quality of the part.

## See Also

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
