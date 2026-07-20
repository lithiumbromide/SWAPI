---
title: "IEdmEnumeratorVariable9 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable9"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9.html"
---

# IEdmEnumeratorVariable9 Interface

Allows you to access the contents of a file data card.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVariable9
   Inherits IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7, IEdmEnumeratorVariable8
```

### C#

```csharp
public interface IEdmEnumeratorVariable9 : IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7, IEdmEnumeratorVariable8
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVariable9 : public IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7, IEdmEnumeratorVariable8
```

## Remarks

This interface:

- extends

  [IEdmEnumeratorVariable8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html)

  by allowing you to set the values of multiple file variables.
- does not support folder data cards. Use

  [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

  and

  [IEdmEnumeratorVariable6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html)

  for folder data cards.
- is extended by

  [IEdmEnumeratorVariable10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable10.html)

  .

See the**Remarks**for[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html).

If you want to update variables in several files or folders, use[IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html), which is more efficient than this interface.

## See Also

[IEdmEnumeratorVariable9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
