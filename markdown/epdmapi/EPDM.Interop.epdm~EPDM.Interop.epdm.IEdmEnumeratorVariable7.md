---
title: "IEdmEnumeratorVariable7 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable7"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7.html"
---

# IEdmEnumeratorVariable7 Interface

Allows you to access the contents of a file data card.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVariable7
   Inherits IEdmEnumeratorVariable5, IEdmEnumeratorVariable6
```

### C#

```csharp
public interface IEdmEnumeratorVariable7 : IEdmEnumeratorVariable5, IEdmEnumeratorVariable6
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVariable7 : public IEdmEnumeratorVariable5, IEdmEnumeratorVariable6
```

## Examples

See the example for

[IEdmEnumeratorVariable8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html)

.

## Remarks

This interface:

- extends

  [IEdmEnumeratorVariable6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html)

  by providing the ability to generate default values, get values of versioned variables, and get the IDs of all variables that have a specified serial number.
- does not support folder data cards. Use

  [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

  and

  [IEdmEnumeratorVariable6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html)

  for folder data cards.
- is extended by

  [IEdmEnumeratorVariable8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html)

  .

See the**Remarks**for[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html).

If you want to update variables in several files or folders, use[IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html), which is more efficient than this interface.

## See Also

[IEdmEnumeratorVariable7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
