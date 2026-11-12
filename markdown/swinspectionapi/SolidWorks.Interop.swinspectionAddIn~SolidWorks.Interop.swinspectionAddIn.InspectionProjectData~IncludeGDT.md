---
title: "IncludeGDT Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "IncludeGDT"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~IncludeGDT.html"
---

# IncludeGDT Property (InspectionProjectData)

Gets and sets whether to extract geometric tolerance symbols from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeGDT As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
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

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
