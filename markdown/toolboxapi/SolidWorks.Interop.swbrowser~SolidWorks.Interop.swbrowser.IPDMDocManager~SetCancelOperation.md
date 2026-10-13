---
title: "SetCancelOperation Method (IPDMDocManager)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IPDMDocManager"
member: "SetCancelOperation"
kind: "method"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager~SetCancelOperation.html"
---

# SetCancelOperation Method (IPDMDocManager)

Cancels the current operation after any notifications are returned.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCancelOperation( _
   ByVal cancelOp As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMDocManager
Dim cancelOp As System.Integer
Dim value As System.Boolean

value = instance.SetCancelOperation(cancelOp)
```

### C#

```csharp
System.bool SetCancelOperation(
   System.int cancelOp
)
```

### C++/CLI

```cpp
System.bool SetCancelOperation(
   System.int cancelOp
)
```

### Parameters

- `cancelOp`: True to cancel the current operation, false to continue the operation

### Return Value

True if the current operation is canceled, false if not

## VBA Syntax

See [PDMDocManager::SetCancelOperation](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~SetCancelOperation.html).

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

## See Also

[IPDMDocManager Interface](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager.html)
[IPDMDocManager Members](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
