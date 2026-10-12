---
title: "EdmUnlockErrInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockErrInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo.html"
---

# EdmUnlockErrInfo Structure

Contains extended information about an error message.

## Syntax

### Visual Basic

```vb
Public Structure EdmUnlockErrInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmUnlockErrInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmUnlockErrInfo : public System.ValueType
```

## Examples

struct EdmUnlockErrInfo{
integer [mlDocID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo~mlDocID.html);
string [mbsConfigName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo~mbsConfigName.html);
integer [mlVarID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo~mlVarID.html);
string [mbsVarName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo~mbsVarName.html);
};

## Examples

[Prevent Admin from Checking In File (C#)](Prevent_Admin_from_Checking_In_File_Example_CSharp.htm)
[Prevent Admin from Checking In File (VB.NET)](Prevent_Admin_from_Checking_In_File_Example_VBNET.htm)

## Remarks

This struct is displayed with [IEdmUnlockOpCallback::MsgBox](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~MsgBox.html).

## See Also

[EdmUnlockErrInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
