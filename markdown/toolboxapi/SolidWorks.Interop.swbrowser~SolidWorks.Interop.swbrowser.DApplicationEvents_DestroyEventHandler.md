---
title: "DApplicationEvents_DestroyEventHandler Delegate (SolidWorks.Interop.swbrowser)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "DApplicationEvents_DestroyEventHandler"
member: ""
kind: "topic"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.DApplicationEvents_DestroyEventHandler.html"
---

# DApplicationEvents_DestroyEventHandler Delegate (SolidWorks.Interop.swbrowser)

Handles the notification that the Toolbox Browser is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DApplicationEvents_DestroyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DApplicationEvents_DestroyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DApplicationEvents_DestroyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DApplicationEvents_DestroyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

## Visual Basic Application (VBA) Syntax

See [Destroy Event (Application)](ms-its:toolboxapivb6.chm::/ToolboxBrowser~Application~Destroy_EV.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

In the body of this handler, you can destroy all references to the Toolbox Browser before its pointer is deleted.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
