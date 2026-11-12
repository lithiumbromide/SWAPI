---
title: "PreventAutoReNumbering Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "PreventAutoReNumbering"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~PreventAutoReNumbering.html"
---

# PreventAutoReNumbering Property (InspectionProjectData)

Gets and sets whether to re-order balloons when one is removed.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreventAutoReNumbering As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.PreventAutoReNumbering = value

value = instance.PreventAutoReNumbering
```

### C#

```csharp
System.bool PreventAutoReNumbering {get; set;}
```

### C++/CLI

```cpp
property System.bool PreventAutoReNumbering {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to prevent re-ordering of balloons, false to re-order when balloons are added or removed

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
