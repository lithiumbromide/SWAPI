---
title: "Units Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "Units"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~Units.html"
---

# Units Property (CharacteristicsData)

Gets the units for this characteristic's nominal and tolerance values.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Units As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
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

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
