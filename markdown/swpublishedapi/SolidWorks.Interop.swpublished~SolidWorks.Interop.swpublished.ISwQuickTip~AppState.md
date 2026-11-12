---
title: "AppState Method (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "AppState"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~AppState.html"
---

# AppState Method (ISwQuickTip)

Sets the state of the add-in application.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AppState( _
   ByVal state As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim state As System.Integer

instance.AppState(state)
```

### C#

```csharp
void AppState(
   System.int state
)
```

### C++/CLI

```cpp
void AppState(
   System.int state
)
```

### Parameters

- `state`: State of the add-in as defined by the add-in

## VBA Syntax

See [SwQuickTip::AppState](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~AppState.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
