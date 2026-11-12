---
title: "Accept Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Accept"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Accept.html"
---

# Accept Property (ICharacteristicsData)

Gets the threshold of defective units for accepting the entire lot.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Accept As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

value = instance.Accept
```

### C#

```csharp
System.string Accept {get;}
```

### C++/CLI

```cpp
property System.String^ Accept {
   System.String^ get();
}
```

### Property Value

Threshold of defective units for acceptance of the lot

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## Remarks

The threshold is based on the sampling plan you selected for this dimension.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
