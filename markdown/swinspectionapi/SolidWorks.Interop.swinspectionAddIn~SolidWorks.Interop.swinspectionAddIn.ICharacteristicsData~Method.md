---
title: "Method Property (ICharacteristicsData)"
project: "SOLIDWORKS Inspection API Help"
interface: "ICharacteristicsData"
member: "Method"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Method.html"
---

# Method Property (ICharacteristicsData)

Gets and sets the inspection method used for this characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Method As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICharacteristicsData
Dim value As System.String

instance.Method = value

value = instance.Method
```

### C#

```csharp
System.string Method {get; set;}
```

### C++/CLI

```cpp
property System.String^ Method {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of an inspection method

## VBA Syntax

See [CharacteristicsData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~CharacteristicsData_members.html) properties.

## See Also

[ICharacteristicsData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)
[ICharacteristicsData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
