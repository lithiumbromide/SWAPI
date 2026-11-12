---
title: "DisconnectFromSW Method (ISwAddin)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddin"
member: "DisconnectFromSW"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin~DisconnectFromSW.html"
---

# DisconnectFromSW Method (ISwAddin)

Calls this method when SOLIDWORKS is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisconnectFromSW() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddin
Dim value As System.Boolean

value = instance.DisconnectFromSW()
```

### C#

```csharp
System.bool DisconnectFromSW()
```

### C++/CLI

```cpp
System.bool DisconnectFromSW();
```

### Return Value

True if the add-in disconnected successfully, false if not

## VBA Syntax

See [SwAddin::DisconnectFromSW](ms-its:swpublishedapivb6.chm::/swpublished~SwAddin~DisconnectFromSW.html).

## Remarks

This is a pre-notification. Add-ins should perform any clean up inside this event.

When this method is called, remove and release all user-interface items related to this add-in (for example, menus, and toolbars).

## See Also

[ISwAddin Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin.html)
[ISwAddin Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
