---
title: "IncludeWeld Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "IncludeWeld"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~IncludeWeld.html"
---

# IncludeWeld Property (InspectionProjectData)

Gets and sets whether to extract welds from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeWeld As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.IncludeWeld = value

value = instance.IncludeWeld
```

### C#

```csharp
System.bool IncludeWeld {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeWeld {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract welds, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
