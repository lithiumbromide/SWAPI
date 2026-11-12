---
title: "Selected Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Selected"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Selected.html"
---

# Selected Property (ICharacteristicsData)

Gets and sets whether to include this characteristic in the inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property Selected As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.Boolean

instance.Selected = value

value = instance.Selected
```

### C#

```csharp
System.bool Selected {get; set;}
```

### C++/CLI

```cpp
property System.bool Selected {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include, false to not

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
