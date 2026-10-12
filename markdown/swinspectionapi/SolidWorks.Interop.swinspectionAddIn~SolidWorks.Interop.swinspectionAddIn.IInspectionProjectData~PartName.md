---
title: "PartName Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "PartName"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~PartName.html"
---

# PartName Property (IInspectionProjectData)

Gets and sets the part name for this inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.PartName = value

value = instance.PartName
```

### C#

```csharp
System.string PartName {get; set;}
```

### C++/CLI

```cpp
property System.String^ PartName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Part name

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
