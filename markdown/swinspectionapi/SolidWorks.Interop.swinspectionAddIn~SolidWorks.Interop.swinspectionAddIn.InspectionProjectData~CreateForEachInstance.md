---
title: "CreateForEachInstance Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "CreateForEachInstance"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~CreateForEachInstance.html"
---

# CreateForEachInstance Property (InspectionProjectData)

Gets and sets whether to create a separate instance for characteristics having a quantity of more than one.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateForEachInstance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.CreateForEachInstance = value

value = instance.CreateForEachInstance
```

### C#

```csharp
System.bool CreateForEachInstance {get; set;}
```

### C++/CLI

```cpp
property System.bool CreateForEachInstance {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to create separate rows in the inspection report for characteristics of multiplicity, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
