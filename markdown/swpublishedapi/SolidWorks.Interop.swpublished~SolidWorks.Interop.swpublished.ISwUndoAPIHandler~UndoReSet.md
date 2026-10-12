---
title: "UndoReSet Method (ISwUndoAPIHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwUndoAPIHandler"
member: "UndoReSet"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwUndoAPIHandler~UndoReSet.html"
---

# UndoReSet Method (ISwUndoAPIHandler)

Resets (clears) the add-in application's undo list after processing the add-in application's undo command and lets an add-in application know that its undo list has been reset.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UndoReSet()
```

### Visual Basic (Usage)

```vb
Dim instance As ISwUndoAPIHandler

instance.UndoReSet()
```

### C#

```csharp
void UndoReSet()
```

### C++/CLI

```cpp
void UndoReSet();
```

## VBA Syntax

See [SwUndoAPIHandler::UndoReSet](ms-its:swpublishedapivb6.chm::/swpublished~swundoapihandler~undoreset.html).

## Examples

[Automate Add-in's Undo Commands (VBA)](Automate_Add-in's_Undo_Commands_Example_VB.htm)

## See Also

[ISwUndoAPIHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwUndoAPIHandler.html)
[ISwUndoAPIHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwUndoAPIHandler_members.html)
