---
title: "IEdmBatchListing3 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing3"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3.html"
---

# IEdmBatchListing3 Interface

Allows you to create a listing of several file, folder, or internal component properties all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchListing3
   Inherits IEdmBatchListing, IEdmBatchListing2
```

### C#

```csharp
public interface IEdmBatchListing3 : IEdmBatchListing, IEdmBatchListing2
```

### C++/CLI

```cpp
public interface class IEdmBatchListing3 : public IEdmBatchListing, IEdmBatchListing2
```

## Remarks

This interface:

- extends [IEdmBatchListing2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2.html) by adding the ability to add an internal component to the listing and get references.
- is extended by [IEdmBatchListing4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4.html), which allows users to find out if files in their local cache are valid or obsolete.

## See Also

[IEdmBatchListing3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
