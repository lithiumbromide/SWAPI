---
title: "DocumentNumber Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "DocumentNumber"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~DocumentNumber.html"
---

# DocumentNumber Property (IInspectionProjectData)

Gets and sets the document number for this inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property DocumentNumber As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.DocumentNumber = value

value = instance.DocumentNumber
```

### C#

```csharp
System.string DocumentNumber {get; set;}
```

### C++/CLI

```cpp
property System.String^ DocumentNumber {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Document number

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
