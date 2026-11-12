---
title: "DocumentRevision Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "DocumentRevision"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~DocumentRevision.html"
---

# DocumentRevision Property (IInspectionProjectData)

Gets and sets the document revision for this inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property DocumentRevision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.DocumentRevision = value

value = instance.DocumentRevision
```

### C#

```csharp
System.string DocumentRevision {get; set;}
```

### C++/CLI

```cpp
property System.String^ DocumentRevision {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Document revision

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
