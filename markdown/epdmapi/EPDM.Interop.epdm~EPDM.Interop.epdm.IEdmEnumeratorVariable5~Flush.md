---
title: "Flush Method (IEdmEnumeratorVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: "Flush"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~Flush.html"
---

# Flush Method (IEdmEnumeratorVariable5)

Saves data to a file or folder.

## Syntax

### Visual Basic

```vb
Sub Flush()
```

### C#

```csharp
void Flush()
```

### C++/CLI

```cpp
void Flush();
```

## Examples

See the example for [IEdmEnumeratorVariable8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html).

## Remarks

You must call this method after calling [IEdmEnumeratorVariable5::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~SetVar.html) to ensure that new data gets properly saved.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_SHARE_ERROR: The file is opened exclusively in another application.

## See Also

[IEdmEnumeratorVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)
[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
