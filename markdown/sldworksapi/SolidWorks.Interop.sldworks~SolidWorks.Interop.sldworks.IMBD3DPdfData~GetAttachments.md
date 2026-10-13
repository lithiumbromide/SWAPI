---
title: "GetAttachments Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "GetAttachments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetAttachments.html"
---

# GetAttachments Method (IMBD3DPdfData)

Gets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Object

value = instance.GetAttachments()
```

### C#

```csharp
System.object GetAttachments()
```

### C++/CLI

```cpp
System.Object^ GetAttachments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the fully qualified paths of the files to include as attachments

## VBA Syntax

See [MBD3DPdfData::GetAttachments](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~GetAttachments.html).

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::SetAttachments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetAttachments.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
