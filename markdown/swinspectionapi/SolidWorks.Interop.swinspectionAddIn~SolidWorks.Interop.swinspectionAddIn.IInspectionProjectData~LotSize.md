---
title: "LotSize Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "LotSize"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~LotSize.html"
---

# LotSize Property (IInspectionProjectData)

Gets and sets the sampling lot size for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property LotSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Integer

instance.LotSize = value

value = instance.LotSize
```

### C#

```csharp
System.int LotSize {get; set;}
```

### C++/CLI

```cpp
property System.int LotSize {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Lot size

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
