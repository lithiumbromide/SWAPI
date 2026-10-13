---
title: "PartRevision Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "PartRevision"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~PartRevision.html"
---

# PartRevision Property (IInspectionProjectData)

Gets and sets the part revision for this inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartRevision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.PartRevision = value

value = instance.PartRevision
```

### C#

```csharp
System.string PartRevision {get; set;}
```

### C++/CLI

```cpp
property System.String^ PartRevision {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Part revision

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
