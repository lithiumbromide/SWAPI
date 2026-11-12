---
title: "OnUserResponseB Method (IMessageBarHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IMessageBarHandler"
member: "OnUserResponseB"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler~OnUserResponseB.html"
---

# OnUserResponseB Method (IMessageBarHandler)

Called by SOLIDWORKS when the user selects the second response control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnUserResponseB( _
   ByVal DoNotShowAgain As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarHandler
Dim DoNotShowAgain As System.Boolean

instance.OnUserResponseB(DoNotShowAgain)
```

### C#

```csharp
void OnUserResponseB(
   System.bool DoNotShowAgain
)
```

### C++/CLI

```cpp
void OnUserResponseB(
   System.bool DoNotShowAgain
)
```

### Parameters

- `DoNotShowAgain`: True to check "Don't Show Again", false to not

## VBA Syntax

See [MessageBarHandler::OnUserResponseB](ms-its:swpublishedapivb6.chm::/swpublished~MessageBarHandler~OnUserResponseB.html).

## Examples

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## See Also

[IMessageBarHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html)
[IMessageBarHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
