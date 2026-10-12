---
title: "DPDMDocManagerEvents_AfterWritingToDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_AfterWritingToDocumentEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_AfterWritingToDocumentEventHandler.html"
---

# DPDMDocManagerEvents_AfterWritingToDocumentEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified PDM-managed document was written to.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_AfterWritingToDocumentEventHandler( _
   ByVal fileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_AfterWritingToDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_AfterWritingToDocumentEventHandler(
   System.string fileName
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_AfterWritingToDocumentEventHandler(
   System.String^ fileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `fileName`: Path and file name of document written to

## Visual Basic Application (VBA) Syntax

See [AfterWritingToDocument Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~AfterWritingToDocument_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

In the body of this handler, you can perform PDM document management functions such as:

- Determine the availability of fileName in the SOLIDWORKS Toolbox.
- Copy a working file to the PDM-managed location, overwriting the PDM-managed version if necessary.
- Set the read-only attribute of the PDM-managed file.

Before returning from this handler, you must call [IPDMDocManager::SetDocumentStatus](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager~SetDocumentStatus.html) with [swPDMStatus_e.swPDMStatusKnownAndAvailable](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.swPDMStatus_e.html) in order to not generate an error.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
