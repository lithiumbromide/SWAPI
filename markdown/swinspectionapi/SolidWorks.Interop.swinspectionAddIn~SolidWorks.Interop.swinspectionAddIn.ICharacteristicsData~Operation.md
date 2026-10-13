---
title: "Operation Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Operation"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Operation.html"
---

# Operation Property (ICharacteristicsData)

Gets and sets the inspection process used for this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Operation As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
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

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
