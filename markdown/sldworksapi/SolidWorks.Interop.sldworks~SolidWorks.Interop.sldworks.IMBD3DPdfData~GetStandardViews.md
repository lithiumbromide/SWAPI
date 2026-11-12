---
title: "GetStandardViews Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "GetStandardViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.html"
---

# GetStandardViews Method (IMBD3DPdfData)

Gets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStandardViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Object

value = instance.GetStandardViews()
```

### C#

```csharp
System.object GetStandardViews()
```

### C++/CLI

```cpp
System.Object^ GetStandardViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the types of standard views as defined in [swStandardViews_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStandardViews_e.html)

## VBA Syntax

See [MBD3DPdfData::GetStandardViews](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~GetStandardViews.html).

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::GetMoreViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.html)
[IMBD3DPdfData::SetMoreViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.html)
[IMBD3DPdfData::SetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
