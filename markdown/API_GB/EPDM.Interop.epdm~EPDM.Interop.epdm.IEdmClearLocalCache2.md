---
title: "IEdmClearLocalCache2 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmClearLocalCache2"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache2.html"
---

# IEdmClearLocalCache2 Interface

Removes specified checked-in files and folders from the local file vault view cache. Only files that are not referenced by checked-out files are cleared.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmClearLocalCache2
   Inherits IEdmClearLocalCache
```

### C#

```csharp
public interface IEdmClearLocalCache2 : IEdmClearLocalCache
```

### C++/CLI

```cpp
public interface class IEdmClearLocalCache2 : public IEdmClearLocalCache
```

## Examples

See the [IEdmClearLocalCache](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache.html) examples.

## Remarks

This interface:

- extends [IEdmClearLocalCache](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache.html) by providing the ability to not remove Toolbox Library parts from the cache.
- is extended by [IEdmClearLocalCache3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache3.html).

## See Also

[IEdmClearLocalCache2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
