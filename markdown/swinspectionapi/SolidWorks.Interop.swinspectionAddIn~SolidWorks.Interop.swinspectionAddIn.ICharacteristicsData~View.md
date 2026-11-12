---
title: "View Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "View"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~View.html"
---

# View Property (ICharacteristicsData)

Gets the SOLIDWORKS drawing view with which this characteristic is associated.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property View As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
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

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
