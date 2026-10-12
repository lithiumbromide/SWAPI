---
title: "Reference Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Reference"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Reference.html"
---

# Reference Property (ICharacteristicsData)

Gets and sets whether this characteristic is a reference dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reference As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.Boolean

instance.Reference = value

value = instance.Reference
```

### C#

```csharp
System.bool Reference {get; set;}
```

### C++/CLI

```cpp
property System.bool Reference {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if a reference dimension, false if not

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
