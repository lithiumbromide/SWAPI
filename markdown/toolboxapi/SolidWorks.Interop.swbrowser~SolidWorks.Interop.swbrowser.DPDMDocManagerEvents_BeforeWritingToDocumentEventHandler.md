---
title: "DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler.html"
---

# DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified PDM-managed document is about to be written to.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler( _
   ByVal fileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler(
   System.string fileName
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler(
   System.String^ fileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `fileName`: Path and file name of document to which to write

### Return Value

If 0 is returned without setting the document status, an error occurs. If 1 is returned, Toolbox uses the specified file name and proceeds as usual.

## Visual Basic Application (VBA) Syntax

See [BeforeWritingToDocument Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~BeforeWritingToDocument_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

In the body of this handler, you can perform PDM document management functions such as:

- Determine the availability of fileName in the SOLIDWORKS Toolbox.
- Clear the read-only attribute of the PDM-managed document in preparation for writing.
- Call [IPDMDocManager::SetManagedDocument](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager~SetManagedDocument.html) to direct the Toolbox Browser application to write to a different document, if the PDM-managed version is not writable.

Before returning from this handler, you must call [IPDMDocManager::SetDocumentStatus](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager~SetDocumentStatus.html) with [swPDMStatus_e.swPDMStatusKnownAndAvailable](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.swPDMStatus_e.html) in order to not generate an error.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
