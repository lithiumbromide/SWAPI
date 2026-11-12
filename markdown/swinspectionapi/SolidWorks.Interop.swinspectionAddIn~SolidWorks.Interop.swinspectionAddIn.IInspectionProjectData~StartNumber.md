---
title: "StartNumber Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "StartNumber"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~StartNumber.html"
---

# StartNumber Property (IInspectionProjectData)

Gets and sets the starting balloon number for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Integer

instance.StartNumber = value

value = instance.StartNumber
```

### C#

```csharp
System.int StartNumber {get; set;}
```

### C++/CLI

```cpp
property System.int StartNumber {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Starting balloon number

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
