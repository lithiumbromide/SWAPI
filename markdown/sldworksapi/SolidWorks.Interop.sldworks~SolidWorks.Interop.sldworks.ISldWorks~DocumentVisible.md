---
title: "DocumentVisible Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DocumentVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DocumentVisible.html"
---

# DocumentVisible Method (ISldWorks)

Allows the application to control the display of a document in a window upon creation or retrieval.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DocumentVisible( _
   ByVal Visible As System.Boolean, _
   ByVal Type As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Visible As System.Boolean
Dim Type As System.Integer

instance.DocumentVisible(Visible, Type)
```

### C#

```csharp
void DocumentVisible(
   System.bool Visible,
   System.int Type
)
```

### C++/CLI

```cpp
void DocumentVisible(
   System.bool Visible,
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visible`: True if the documents of the specified type are displayed upon creation or retrieval, false if not
- `Type`: Type of document to which you apply visibility as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

## VBA Syntax

See [SldWorks::DocumentVisible](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DocumentVisible.html).

## Remarks

This method is a flag that allows you to display or hide documents as they are loaded.

If you create a document invisibly by passing false to this method, then you cannot make it visible with [IModelDoc2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Visible.html). Instead you should close it and then reopen it as a visible document.

Additionally if SOLIDWORKS was hidden by a call to [ISldWorks::UserControlBackground](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~UserControlBackground.html), and a document is opened (e.g., a configuration is loaded), then you must call this method to keep the SOLIDWORKS Design user interface hidden.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.html)
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.html)
