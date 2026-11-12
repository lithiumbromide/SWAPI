---
title: "EdmUpdatedRefPath Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUpdatedRefPath"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUpdatedRefPath.html"
---

# EdmUpdatedRefPath Structure

Contains old and new path information for references that are moved or renamed by another client.

## Syntax

### Visual Basic

```vb
Public Structure EdmUpdatedRefPath
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmUpdatedRefPath : System.ValueType
```

### C++/CLI

```cpp
public value class EdmUpdatedRefPath : public System.ValueType
```

## Examples

struct EdmUpdatedRefPath{
string [mbsRefOldPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUpdatedRefPath~mbsRefOldPath.html);
string [mbsRefNewPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUpdatedRefPath~mbsRefNewPath.html);
};

## Remarks

This structure is returned by [IEdmRefItem2::GetUpdatedPaths](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2~GetUpdatedPaths.html).

## See Also

[EdmUpdatedRefPath Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUpdatedRefPath_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP04
