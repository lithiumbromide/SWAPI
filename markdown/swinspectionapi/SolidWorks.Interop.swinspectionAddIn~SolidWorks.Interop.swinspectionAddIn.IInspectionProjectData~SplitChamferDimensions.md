---
title: "SplitChamferDimensions Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "SplitChamferDimensions"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~SplitChamferDimensions.html"
---

# SplitChamferDimensions Property (IInspectionProjectData)

Gets and sets whether to treat each part of a chamfer dimension as a separate characteristic for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitChamferDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.SplitChamferDimensions = value

value = instance.SplitChamferDimensions
```

### C#

```csharp
System.bool SplitChamferDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool SplitChamferDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to create separate rows for the linear dimension and angle of a chamfer dimension, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
