---
title: "EdmAddInFileInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddInFileInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo.html"
---

# EdmAddInFileInfo Structure

Contains information about a single file in an add-in package.

## Syntax

### Visual Basic

```vb
Public Structure EdmAddInFileInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmAddInFileInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmAddInFileInfo : public System.ValueType
```

## Examples

struct EdmAddInFileInfo{
string [mbsFileName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo~mbsFileName.html);
integer [mlEdmAddInFileInfoFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo~mlEdmAddInFileInfoFlags.html);
};

## Examples

[Install Add-in (VB.NET)](Load_Addin_Example_VBNET.htm)
[Install Add-in (C#)](Load_Addin_Example_CSharp.htm)

## Remarks

Returned by [IEdmAddInMgr8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8.html).

## See Also

[EdmAddInFileInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
