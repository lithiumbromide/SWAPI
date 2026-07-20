---
title: "IEdmEnumeratorVariable10 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable10"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable10.html"
---

# IEdmEnumeratorVariable10 Interface

Allows you to access the contents of a file data card.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVariable10
   Inherits IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7, IEdmEnumeratorVariable8, IEdmEnumeratorVariable9
```

### C#

```csharp
public interface IEdmEnumeratorVariable10 : IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7, IEdmEnumeratorVariable8, IEdmEnumeratorVariable9
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVariable10 : public IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7, IEdmEnumeratorVariable8, IEdmEnumeratorVariable9
```

## Remarks

This interface:

- extends

  [IEdmEnumeratorVariable9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9.html)

  by providing the ability to get a card variable from a file shared across multiple folders or get a card variable value in text format for a file shared across multiple folders.
- does not support folder data cards. Use

  [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

  and

  [IEdmEnumeratorVariable6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html)

  for folder data cards.

See the**Remarks**for[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html).

If you want to update variables in several files or folders, use[IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html), which is more efficient than this interface.

## See Also

[IEdmEnumeratorVariable10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable10_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
