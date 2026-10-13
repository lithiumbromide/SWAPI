---
title: "DPDMDocManagerEvents_NewDocumentAddedEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_NewDocumentAddedEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_NewDocumentAddedEventHandler.html"
---

# DPDMDocManagerEvents_NewDocumentAddedEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the specified part was added to the Toolbox.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_NewDocumentAddedEventHandler( _
   ByVal fileName As System.String, _
   ByVal ToolboxID As System.Integer, _
   ByVal AddedToBrowser As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_NewDocumentAddedEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_NewDocumentAddedEventHandler(
   System.string fileName,
   System.int ToolboxID,
   System.int AddedToBrowser
)
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_NewDocumentAddedEventHandler(
   System.String^ fileName,
   System.int ToolboxID,
   System.int AddedToBrowser
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `fileName`: Path and file name of the new part
- `ToolboxID`: ID is calculated for copied part creation; otherwise 1
- `AddedToBrowser`: True if the the part resides in the SOLIDWORKS Toolbox database, false if not

## Visual Basic Application (VBA) Syntax

See [NewDocumentAdded Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~NewDocumentAdded_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

In this handler, call [IPDMDocManager:SetManagedDocument](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager~SetManagedDocument.html) to direct the Toolbox Browser application to use the new document. For copied parts, the file inserted into the assembly is the IPDMDocManager::SetManagedDocument filename.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
