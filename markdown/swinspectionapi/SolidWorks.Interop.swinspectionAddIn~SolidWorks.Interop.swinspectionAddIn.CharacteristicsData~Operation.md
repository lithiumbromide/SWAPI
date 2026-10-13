---
title: "Operation Property (CharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "CharacteristicsData"
member: "Operation"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData~Operation.html"
---

# Operation Property (CharacteristicsData)

Gets and sets the inspection process used for this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Operation As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CharacteristicsData
Dim value As System.String

instance.Operation = value

value = instance.Operation
```

### C#

```csharp
System.string Operation {get; set;}
```

### C++/CLI

```cpp
property System.String^ Operation {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of an inspection operation

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[CharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData.html)
[CharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.CharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
