---
title: "Sort Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "Sort"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~Sort.html"
---

# Sort Property (InspectionProjectData)

Gets and sets the ballooning arrangement for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Sort As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Integer

instance.Sort = value

value = instance.Sort
```

### C#

```csharp
System.int Sort {get; set;}
```

### C++/CLI

```cpp
property System.int Sort {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Ballooning arrangement as defined by [swiCharacteristicInfoSort_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicInfoSort_e.html)

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
