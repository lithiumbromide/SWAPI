---
title: "DPDMDocManagerEvents_PreInsertDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_PreInsertDocumentEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_PreInsertDocumentEventHandler.html"
---

# DPDMDocManagerEvents_PreInsertDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified PDM-managed document is about to be inserted into an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_PreInsertDocumentEventHandler( _
   ByVal fileName As System.String, _
   ByVal ToolboxID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_PreInsertDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_PreInsertDocumentEventHandler(
   System.string fileName,
   System.int ToolboxID
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_PreInsertDocumentEventHandler(
   System.String^ fileName,
   System.int ToolboxID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `fileName`: Path and file name of the document to insert
- `ToolboxID`: ID is calculated for copied part creation; otherwise 1

## Visual Basic Application (VBA) Syntax

See [PreInsertDocument Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~PreInsertDocument_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

Works like the SOLIDWORKS FileDropPreNotify event for the [SmartFastener](GettingStarted-toolboxapi.html#Insert). If a file with the same name is already open in SOLIDWORKS, Toolbox uses that file and does not send the PreInsertDocument notification.

Before returning from this handler, you must call [IPDMDocManager::SetManagedDocument](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager~SetManagedDocument.html). The PDM application can use this method to direct the Toolbox Browser application to work with a file other than the PDM-managed document, which may not be writable. If the file does not exist, SOLIDWORKS generates an error and aborts all operations. If this file name is null for copied parts, SOLIDWORKS creates a new part. For all other insertions, SOLIDWORKS uses the original file name when an empty file name is specified.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
