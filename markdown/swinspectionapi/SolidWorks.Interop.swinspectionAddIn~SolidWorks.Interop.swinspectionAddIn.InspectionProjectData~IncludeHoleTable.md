---
title: "IncludeHoleTable Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "IncludeHoleTable"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~IncludeHoleTable.html"
---

# IncludeHoleTable Property (InspectionProjectData)

Gets and sets whether to extract hole tables from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHoleTable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.IncludeHoleTable = value

value = instance.IncludeHoleTable
```

### C#

```csharp
System.bool IncludeHoleTable {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeHoleTable {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract hole tables, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
