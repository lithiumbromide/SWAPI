---
title: "LowerLimit Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "LowerLimit"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~LowerLimit.html"
---

# LowerLimit Property (ICharacteristicsData)

Gets and sets the absolute lower limit of this characteristic's dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerLimit As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.LowerLimit = value

value = instance.LowerLimit
```

### C#

```csharp
System.string LowerLimit {get; set;}
```

### C++/CLI

```cpp
property System.String^ LowerLimit {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Absolute lower limit

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## Remarks

The absolute lower limit of a dimension is its nominal value minus its lower tolerance value.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
