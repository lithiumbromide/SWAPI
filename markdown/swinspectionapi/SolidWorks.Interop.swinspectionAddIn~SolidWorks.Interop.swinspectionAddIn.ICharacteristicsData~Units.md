---
title: "Units Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Units"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Units.html"
---

# Units Property (ICharacteristicsData)

Gets the units for this characteristic's nominal and tolerance values.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Units As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

value = instance.Units
```

### C#

```csharp
System.string Units {get;}
```

### C++/CLI

```cpp
property System.String^ Units {
   System.String^ get();
}
```

### Property Value

Units of nominal and tolerance values:

"in"

"mm"

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
