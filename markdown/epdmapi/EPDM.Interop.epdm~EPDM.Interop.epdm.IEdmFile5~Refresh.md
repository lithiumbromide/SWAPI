---
title: "Refresh Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "Refresh"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~Refresh.html"
---

# Refresh Method (IEdmFile5)

Refreshes the file.

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

In a multi-user implementation, a file can be checked in and out by others while you are working on it. Call this method before calling [IEdmFile5::IsLocked](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~IsLocked.html) to obtain the correct checkout status.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
