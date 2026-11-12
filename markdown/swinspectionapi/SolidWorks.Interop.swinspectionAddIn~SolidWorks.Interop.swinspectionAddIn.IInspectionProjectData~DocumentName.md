---
title: "DocumentName Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "DocumentName"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~DocumentName.html"
---

# DocumentName Property (IInspectionProjectData)

Gets and sets the document name for this inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property DocumentName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.DocumentName = value

value = instance.DocumentName
```

### C#

```csharp
System.string DocumentName {get; set;}
```

### C++/CLI

```cpp
property System.String^ DocumentName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Document name

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
