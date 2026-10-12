---
title: "JobNumber Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "JobNumber"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~JobNumber.html"
---

# JobNumber Property (IInspectionProjectData)

Gets and sets the job number for this inspection report.

## Syntax

### Visual Basic (Declaration)

```vb
Property JobNumber As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.JobNumber = value

value = instance.JobNumber
```

### C#

```csharp
System.string JobNumber {get; set;}
```

### C++/CLI

```cpp
property System.String^ JobNumber {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Job number

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
