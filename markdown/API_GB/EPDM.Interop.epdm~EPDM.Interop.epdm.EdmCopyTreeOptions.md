---
title: "EdmCopyTreeOptions Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCopyTreeOptions"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions.html"
---

# EdmCopyTreeOptions Structure

Contains options for copying an assembly tree of files to a destination folder.

## Syntax

### Visual Basic

```vb
Public Structure EdmCopyTreeOptions
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCopyTreeOptions : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCopyTreeOptions : public System.ValueType
```

## Examples

struct EdmCmdInfo

{
string [mbsPrefix](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions~mbsPrefix.html);
string [mbsSuffix](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions~mbsSuffix.html);
VARIANT_BOOL [mbIncludeDrawings](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions~mbIncludeDrawings.html);
VARIANT_BOOL [mbUseLatestVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions~mbUseLatestVersion.html);
};

## Examples

[Copy Assembly Tree of Files (VB.NET)](Copy_Assembly_Tree_Example_VBNET.htm)
[Copy Assembly Tree of Files (C#)](Copy_Assembly_Tree_Example_CSharp.htm)

## See Also

[EdmCopyTreeOptions Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
