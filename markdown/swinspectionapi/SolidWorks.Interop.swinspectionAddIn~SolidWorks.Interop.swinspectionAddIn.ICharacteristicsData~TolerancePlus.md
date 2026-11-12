---
title: "TolerancePlus Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "TolerancePlus"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~TolerancePlus.html"
---

# TolerancePlus Property (ICharacteristicsData)

Gets and sets this characteristic's upper tolerance value.

## Syntax

### Visual Basic (Declaration)

```vb
Property TolerancePlus As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.TolerancePlus = value

value = instance.TolerancePlus
```

### C#

```csharp
System.string TolerancePlus {get; set;}
```

### C++/CLI

```cpp
property System.String^ TolerancePlus {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Upper tolerance value

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
