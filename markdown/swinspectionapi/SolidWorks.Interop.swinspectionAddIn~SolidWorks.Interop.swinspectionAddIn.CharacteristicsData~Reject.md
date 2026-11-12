---
title: "Reject Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "Reject"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~Reject.html"
---

# Reject Property (CharacteristicsData)

Gets the threshold of defective units for rejecting the entire lot.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Reject As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
Dim value As System.String

value = instance.Reject
```

### C#

```csharp
System.string Reject {get;}
```

### C++/CLI

```cpp
property System.String^ Reject {
   System.String^ get();
}
```

### Property Value

Threshold of defective units for rejecting the entire lot

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## Remarks

The threshold is based on the sampling plan you selected for this dimension.

## See Also

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
