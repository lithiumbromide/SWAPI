---
title: "ConnectToSW Method (ISwAddin)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddin"
member: "ConnectToSW"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin~ConnectToSW.html"
---

# ConnectToSW Method (ISwAddin)

Calls this method when the add-in is loaded.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConnectToSW( _
   ByVal ThisSW As System.Object, _
   ByVal Cookie As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddin
Dim ThisSW As System.Object
Dim Cookie As System.Integer
Dim value As System.Boolean

value = instance.ConnectToSW(ThisSW, Cookie)
```

### C#

```csharp
System.bool ConnectToSW(
   System.object ThisSW,
   System.int Cookie
)
```

### C++/CLI

```cpp
System.bool ConnectToSW(
   System.Object^ ThisSW,
   System.int Cookie
)
```

### Parameters

- `ThisSW`: Pointer to the SldWorks Dispatch object
- `Cookie`: Add-in ID

### Return Value

True if the add-in connected successfully, false if not

## VBA Syntax

See [SwAddin::ConnectToSW](ms-its:swpublishedapivb6.chm::/swpublished~SwAddin~ConnectToSW.html).

## Remarks

When this method is called, add all required items for this add-in to the SOLIDWORKS user interface (for example, menus and toolbars) and set the event handler.

[ISldWorks::ExitApp](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.html) does not work if called from within this method.

## See Also

[ISwAddin Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin.html)
[ISwAddin Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
