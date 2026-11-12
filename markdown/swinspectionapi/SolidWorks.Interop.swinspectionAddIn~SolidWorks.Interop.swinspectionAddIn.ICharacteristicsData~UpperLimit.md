---
title: "UpperLimit Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "UpperLimit"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~UpperLimit.html"
---

# UpperLimit Property (ICharacteristicsData)

Gets and sets the absolute upper limit of this characteristic's dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperLimit As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.UpperLimit = value

value = instance.UpperLimit
```

### C#

```csharp
System.string UpperLimit {get; set;}
```

### C++/CLI

```cpp
property System.String^ UpperLimit {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Absolute upper limit

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## Remarks

The absolute upper limit of a dimension is its nominal value plus its upper tolerance value.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
