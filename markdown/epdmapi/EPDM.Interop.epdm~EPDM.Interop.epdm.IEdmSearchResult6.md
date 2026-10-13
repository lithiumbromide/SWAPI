---
title: "IEdmSearchResult6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult6"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6.html"
---

# IEdmSearchResult6 Interface

Allows you to access a search result.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmSearchResult6
   Inherits IEdmObject5, IEdmSearchResult5
```

### C#

```csharp
public interface IEdmSearchResult6 : IEdmObject5, IEdmSearchResult5
```

### C++/CLI

```cpp
public interface class IEdmSearchResult6 : public IEdmObject5, IEdmSearchResult5
```

## Examples

See the [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html) examples.

## Remarks

This interface extends [IEdmSearchResult5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html).

To use this interface:

1. Call [IEdmSearch10::GetFirstFavoriteResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10~GetFirstFavoriteResult.html), specifying a favorite search name and whether to get search result custom column information.
2. Determine the type of the search result returned in step 1 by inspecting [ObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~ObjectType.html). (Becaue IEdmSearchResult5 inherits from IEdmObject5, you can simply call IEdmSearchResult5::ObjectType.)
3. If the type of this search result is an:

  1. [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_File, cast the search result object to [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html).
  2. EdmObjectType.EdmObject_Folder, cast the search result object to [IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html).
4. Cast the search result object obtained in step 1 to an IEdmSearchResult6 object. Call [IEdmSearchResult6::GetCustomColumnsInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnsInfo.html) and [IEdmSearchResult6::GetCustomColumnValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnValues.html) to obtain custom column information for the search result listing.

## See Also

[IEdmSearchResult6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
