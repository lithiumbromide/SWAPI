---
title: "DPDMDocManagerEvents_DestroyEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DPDMDocManagerEvents_DestroyEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DPDMDocManagerEvents_DestroyEventHandler.html"
---

# DPDMDocManagerEvents_DestroyEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the PDM application object is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPDMDocManagerEvents_DestroyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPDMDocManagerEvents_DestroyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPDMDocManagerEvents_DestroyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPDMDocManagerEvents_DestroyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

## Visual Basic Application (VBA) Syntax

See [Destroy Event (PDMDocManager)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~Destroy_EV.html)

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

In the body of this handler, you can destroy all references to the PDM application before its pointer is deleted.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
