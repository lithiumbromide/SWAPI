---
title: "DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler.html"
---

# DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified PDM-managed document is about to be copied to the specified new file name.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler( _
   ByVal FromFileName As System.String, _
   ByVal ToFileName As System.String, _
   ByVal DeleteSource As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler(
   System.string FromFileName,
   System.string ToFileName,
   System.int DeleteSource
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler(
   System.String^ FromFileName,
   System.String^ ToFileName,
   System.int DeleteSource
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `FromFileName`: Path and file name of document to copy
- `ToFileName`: Path and file name of of the new document
- `DeleteSource`: True to delete FromFileName, false to not

## Visual Basic Application (VBA) Syntax

See [BeforeCopyingDocument Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~BeforeCopyingDocument_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
