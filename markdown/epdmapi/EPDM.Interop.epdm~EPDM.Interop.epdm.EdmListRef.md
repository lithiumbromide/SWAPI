---
title: "EdmListRef Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListRef"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListRef.html"
---

# EdmListRef Structure

Contains information about file references.

## Syntax

### Visual Basic

```vb
Public Structure EdmListRef
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmListRef : System.ValueType
```

### C++/CLI

```cpp
public value class EdmListRef : public System.ValueType
```

## Examples

```
struct EdmListRef
{
  integer mlChildID;
  integer mlChildFolderID;
  integer mlChildRefVersion;
  integer mlParentFileID;
  integer mlParentFolderID;};
```

## Remarks

Returned by [IEdmBatchListing3::GetReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3~GetReferences.html).

## See Also

[EdmListRef Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListRef_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2014
