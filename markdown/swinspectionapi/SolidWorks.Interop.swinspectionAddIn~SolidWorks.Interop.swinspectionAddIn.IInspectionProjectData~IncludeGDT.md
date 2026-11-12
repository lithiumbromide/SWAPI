---
title: "IncludeGDT Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "IncludeGDT"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeGDT.html"
---

# IncludeGDT Property (IInspectionProjectData)

Gets and sets whether to extract geometric tolerance symbols from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeGDT As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.IncludeGDT = value

value = instance.IncludeGDT
```

### C#

```csharp
System.bool IncludeGDT {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeGDT {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract GTols, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
