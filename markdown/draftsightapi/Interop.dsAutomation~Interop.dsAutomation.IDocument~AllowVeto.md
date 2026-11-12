---
title: "AllowVeto Method (IDocument)"
project: ""
interface: "IDocument"
member: "AllowVeto"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~AllowVeto.html"
---

# AllowVeto Method (IDocument)

Sets whether to abort a command operation.

## Syntax

### Visual Basic

```vb
Sub AllowVeto( _
   ByVal Val As System.Boolean _
)
```

### C#

```csharp
void AllowVeto(
   System.bool Val
)
```

### JScript

```
function AllowVeto(
   Val : System.boolean
);
```

### Managed Extensions for C++

```
void AllowVeto(
   System.bool Val
)
```

### C++/CLI

```cpp
void AllowVeto(
   System.bool Val
)
```

### Parameters

- `Val`: True to abort, false to not

## Remarks

Call this method from within the [_IApplicationEvents_CommandPreNotifyEventHandler](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPreNotifyEventHandler.html).

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight 2020 SP0
