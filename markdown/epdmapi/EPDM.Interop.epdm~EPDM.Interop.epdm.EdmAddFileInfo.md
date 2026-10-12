---
title: "EdmAddFileInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddFileInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo.html"
---

# EdmAddFileInfo Structure

Contains information about a file.

## Syntax

### Visual Basic

```vb
Public Structure EdmAddFileInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmAddFileInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmAddFileInfo : public System.ValueType
```

## Examples

struct EdmAddFileInfo{
integer [mlSrcDocumentID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mlSrcDocumentID.html);
integer [mlSrcProjectID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mlSrcProjectID.html);
string [mbsPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mbsPath.html);
string [mbsNewName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mbsNewName.html);
integer [mlEdmAddFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mlEdmAddFlags.html);
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mlFileID.html);
};

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

Returned by [IEdmFolder6::AddFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~AddFiles.html).

## See Also

[EdmAddFileInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.0 of SOLIDWORKS PDM Professional
