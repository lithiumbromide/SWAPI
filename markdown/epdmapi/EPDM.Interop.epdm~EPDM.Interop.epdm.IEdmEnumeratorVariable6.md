---
title: "IEdmEnumeratorVariable6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable6"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html"
---

# IEdmEnumeratorVariable6 Interface

Allows you to access the contents of a file or folder data card.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVariable6
   Inherits IEdmEnumeratorVariable5
```

### C#

```csharp
public interface IEdmEnumeratorVariable6 : IEdmEnumeratorVariable5
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVariable6 : public IEdmEnumeratorVariable5
```

## Examples

See the example for

[IEdmEnumeratorVariable8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html)

.

## Remarks

This interface:

- extends

  [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

  by providing the ability to read a variable from the database.
- is extended by

  [IEdmEnumeratorVariable7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7.html)

  .

See the**Remarks**for[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html).

If you want to update variables in several files or folders, use[IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html), which is more efficient than this interface.

## See Also

[IEdmEnumeratorVariable6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
