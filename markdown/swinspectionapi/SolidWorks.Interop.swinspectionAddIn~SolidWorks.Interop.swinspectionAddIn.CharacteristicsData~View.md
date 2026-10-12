---
title: "View Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "View"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~View.html"
---

# View Property (CharacteristicsData)

Gets the SOLIDWORKS drawing view with which this characteristic is associated.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property View As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
Dim value As System.String

value = instance.View
```

### C#

```csharp
System.string View {get;}
```

### C++/CLI

```cpp
property System.String^ View {
   System.String^ get();
}
```

### Property Value

Name of a SOLIDWORKS drawing view

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
