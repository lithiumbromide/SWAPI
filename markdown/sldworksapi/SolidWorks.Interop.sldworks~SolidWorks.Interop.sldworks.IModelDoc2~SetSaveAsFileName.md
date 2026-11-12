---
title: "SetSaveAsFileName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetSaveAsFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveAsFileName.html"
---

# SetSaveAsFileName Method (IModelDoc2)

Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSaveAsFileName( _
   ByVal FileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileName As System.String

instance.SetSaveAsFileName(FileName)
```

### C#

```csharp
void SetSaveAsFileName(
   System.string FileName
)
```

### C++/CLI

```cpp
void SetSaveAsFileName(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: **Save As** filename

## VBA Syntax

See [ModelDoc2::SetSaveAsFileName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetSaveAsFileName.html).

## Remarks

Use this method from within the FileSaveAsNotify2 event handler. When setting the Save As filename using this method, S_false should be returned from the FileSaveAsNotify2 event handler. See [DAssemblyDocEvents FileSaveAsNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.html), [DDrawingDocEvents FileSaveAsNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.html), and [DPartDocEvents FileSaveAsNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.html) notifications.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
