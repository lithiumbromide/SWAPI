---
title: "ExcludeFromAnnotationView Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "ExcludeFromAnnotationView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ExcludeFromAnnotationView.html"
---

# ExcludeFromAnnotationView Property (IMBD3DPdfData)

Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeFromAnnotationView As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Boolean

instance.ExcludeFromAnnotationView = value

value = instance.ExcludeFromAnnotationView
```

### C#

```csharp
System.bool ExcludeFromAnnotationView {get; set;}
```

### C++/CLI

```cpp
property System.bool ExcludeFromAnnotationView {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to exclude BOM tables from annotation views, false to not

## VBA Syntax

See [MBD3DPdfData::ExcludeFromAnnotationView](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~ExcludeFromAnnotationView.html).

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::GetBomAreaCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetBomAreaCount.html)
[IMBD3DPdfData::SetBomTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetBomTable.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
