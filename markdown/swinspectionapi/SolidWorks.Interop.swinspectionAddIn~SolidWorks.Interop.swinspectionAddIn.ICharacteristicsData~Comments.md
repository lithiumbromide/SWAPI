---
title: "Comments Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Comments"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Comments.html"
---

# Comments Property (ICharacteristicsData)

Gets and sets the comment for this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Comments As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.Comments = value

value = instance.Comments
```

### C#

```csharp
System.string Comments {get; set;}
```

### C++/CLI

```cpp
property System.String^ Comments {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Comment

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
