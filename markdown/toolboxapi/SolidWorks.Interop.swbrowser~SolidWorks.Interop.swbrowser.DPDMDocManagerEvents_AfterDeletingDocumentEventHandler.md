---
title: "DPDMDocManagerEvents_AfterDeletingDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_AfterDeletingDocumentEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_AfterDeletingDocumentEventHandler.html"
---

# DPDMDocManagerEvents_AfterDeletingDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified PDM-managed document was deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_AfterDeletingDocumentEventHandler( _
   ByVal fileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_AfterDeletingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_AfterDeletingDocumentEventHandler(
   System.string fileName
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_AfterDeletingDocumentEventHandler(
   System.String^ fileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `fileName`: Path and file name of document deleted

## Visual Basic Application (VBA) Syntax

See [AfterDeletingDocument Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~AfterDeletingDocument_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
