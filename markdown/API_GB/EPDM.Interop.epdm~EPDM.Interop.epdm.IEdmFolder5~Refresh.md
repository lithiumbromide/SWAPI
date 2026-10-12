---
title: "Refresh Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "Refresh"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~Refresh.html"
---

# Refresh Method (IEdmFolder5)

Refreshes the file listing for the folder.

## Syntax

### Visual Basic

```vb
Sub Refresh()
```

### C#

```csharp
void Refresh()
```

### C++/CLI

```cpp
void Refresh();
```

## Remarks

In a multi-user implementation, the contents of this folder may change as you are working on it. Call this method before using other methods of this interface to ensure that you are seeing the latest state of the folder.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
