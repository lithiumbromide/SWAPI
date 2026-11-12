---
title: "DPartDocEvents_EquationEditorPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_EquationEditorPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler.html"
---

# DPartDocEvents_EquationEditorPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your application that an the equation editor has been constructed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_EquationEditorPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_EquationEditorPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_EquationEditorPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_EquationEditorPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [EquationEditorPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~EquationEditorPreNotify_EV.html).

## Remarks

The PartDoc event [EquationEditorPostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_EquationEditorPostNotifyEventHandler.html) notifies your application that is being destroyed.

If developing a C++ application, use [swPartEquationPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
