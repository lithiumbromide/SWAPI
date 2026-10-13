---
title: "DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler.html"
---

# DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified PDM-managed document is about to be deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler( _
   ByVal fileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler(
   System.string fileName
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler(
   System.String^ fileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `fileName`: Path and file name of document to delete

## Visual Basic Application (VBA) Syntax

See [BeforeDeletingDocument Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~BeforeDeletingDocument_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
