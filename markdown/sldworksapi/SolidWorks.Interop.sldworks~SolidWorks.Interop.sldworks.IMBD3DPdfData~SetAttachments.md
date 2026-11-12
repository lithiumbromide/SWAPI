---
title: "SetAttachments Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "SetAttachments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetAttachments.html"
---

# SetAttachments Method (IMBD3DPdfData)

Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAttachments( _
   ByVal Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim Values As System.Object

instance.SetAttachments(Values)
```

### C#

```csharp
void SetAttachments(
   System.object Values
)
```

### C++/CLI

```cpp
void SetAttachments(
   System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Values`: Array of strings of the fully qualified paths of the files to include as attachments

## VBA Syntax

See [MBD3DPdfData::SetAttachments](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~SetAttachments.html).

## Examples

[Attach Files to MBD 3D PDF (C#)](Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm)
[Attach Files to MBD 3D PDF (VB.NET)](Attach_Files_to_MBD_3D_PDF_Example_VBNET.htm)
[Attach Files to MBD 3D PDF (VBA)](Attach_Files_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::GetAttachments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetAttachments.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
