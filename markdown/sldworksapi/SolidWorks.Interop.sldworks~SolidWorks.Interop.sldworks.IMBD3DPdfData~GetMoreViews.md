---
title: "GetMoreViews Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "GetMoreViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.html"
---

# GetMoreViews Method (IMBD3DPdfData)

Gets the names of the custom views (i.e., [named views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.html) and [3D views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)) in the model for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMoreViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Object

value = instance.GetMoreViews()
```

### C#

```csharp
System.object GetMoreViews()
```

### C++/CLI

```cpp
System.Object^ GetMoreViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the names of the custom views

## VBA Syntax

See [MBD3DPdfData::GetMoreViews](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~GetMoreViews.html).

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::GetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.html)
[IMBD3DPdfData::SetMoreViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.html)
[IMBD3DPdfData::SetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
