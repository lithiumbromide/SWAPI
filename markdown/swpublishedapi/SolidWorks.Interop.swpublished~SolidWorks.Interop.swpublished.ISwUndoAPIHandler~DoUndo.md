---
title: "DoUndo Method (ISwUndoAPIHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwUndoAPIHandler"
member: "DoUndo"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwUndoAPIHandler~DoUndo.html"
---

# DoUndo Method (ISwUndoAPIHandler)

Undoes an add-in application's previously processed commands when an end-user selects its undo command on the SOLIDWORKS undo list or it is called in a macro.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DoUndo()
```

### Visual Basic (Usage)

```vb
Dim instance As ISwUndoAPIHandler

instance.DoUndo()
```

### C#

```csharp
void DoUndo()
```

### C++/CLI

```cpp
void DoUndo();
```

## VBA Syntax

See [SwUndoAPIHandler::DoUndo](ms-its:swpublishedapivb6.chm::/swpublished~swundoapihandler~doundo.html).

## Examples

[Automate Add-in's Undo Commands (VBA)](Automate_Add-in's_Undo_Commands_Example_VB.htm)

## See Also

[ISwUndoAPIHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwUndoAPIHandler.html)
[ISwUndoAPIHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwUndoAPIHandler_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
