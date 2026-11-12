---
title: "IncludeHoleTable Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "IncludeHoleTable"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeHoleTable.html"
---

# IncludeHoleTable Property (IInspectionProjectData)

Gets and sets whether to extract hole tables from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHoleTable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
