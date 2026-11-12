---
title: "ToleranceMinus Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "ToleranceMinus"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~ToleranceMinus.html"
---

# ToleranceMinus Property (ICharacteristicsData)

Gets and sets this characteristic's lower tolerance value.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceMinus As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.ToleranceMinus = value

value = instance.ToleranceMinus
```

### C#

```csharp
System.string ToleranceMinus {get; set;}
```

### C++/CLI

```cpp
property System.String^ ToleranceMinus {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Lower tolerance value

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
