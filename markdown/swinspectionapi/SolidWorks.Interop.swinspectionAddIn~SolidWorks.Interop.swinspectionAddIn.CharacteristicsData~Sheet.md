---
title: "Sheet Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "Sheet"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~Sheet.html"
---

# Sheet Property (CharacteristicsData)

Gets the SOLIDWORKS drawing sheet where this characteristic is located.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sheet As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
Dim value As System.String

value = instance.Sheet
```

### C#

```csharp
System.string Sheet {get;}
```

### C++/CLI

```cpp
property System.String^ Sheet {
   System.String^ get();
}
```

### Property Value

Name of a SOLIDWORKS drawing sheet

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
