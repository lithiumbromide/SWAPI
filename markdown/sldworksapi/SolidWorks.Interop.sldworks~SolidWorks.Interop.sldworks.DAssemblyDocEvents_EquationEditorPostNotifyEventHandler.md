---
title: "DAssemblyDocEvents_EquationEditorPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_EquationEditorPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_EquationEditorPostNotifyEventHandler.html"
---

# DAssemblyDocEvents_EquationEditorPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your application that the equation editor is being destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_EquationEditorPostNotifyEventHandler( _
   ByVal Changed As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_EquationEditorPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_EquationEditorPostNotifyEventHandler(
   System.bool Changed
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_EquationEditorPostNotifyEventHandler(
   System.bool Changed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Changed`: True if equations have changed, false if not

## VBA Syntax

See [EquationEditorPostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~EquationEditorPostNotify_EV.html).

## Remarks

The IAssemblyDoc event [EquationEditorPreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_EquationEditorPreNotifyEventHandler.html) notifies your application that the equation editor has been constructed.

If developing a C++ application, use [swAssemblyEquationEditorPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
