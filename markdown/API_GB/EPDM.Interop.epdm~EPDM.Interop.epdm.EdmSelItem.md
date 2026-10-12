---
title: "EdmSelItem Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmSelItem"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html"
---

# EdmSelItem Structure

Contains information about one selected file; e.g., used with [IEdmBatchUnlock::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~AddSelection.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmSelItem
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmSelItem : System.ValueType
```

### C++/CLI

```cpp
public value class EdmSelItem : public System.ValueType
```

## Examples

struct EdmSelItem

{
integer [mlDocID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem~mlDocID.html);
integer [mlProjID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem~mlProjID.html);
};

## Examples

[Batch Check Out Files (VB.NET)](Batch_Get_Files_Example_VBNET.htm)
[Batch Check Out Files (C#)](Batch_Get_Files_Example_CSharp.htm)
[Access Check-in Flags in Check out Dialog (C#)](Access_Check-in_Flags_in_Check_in_Dialog_Example_CSharp.htm)
[Access Check-in Flags in Check out Dialog (VB.NET)](Access_Check-in_Flags_in_Check_in_Dialog_Example_VBNET.htm)
[Prevent Admin from Checking In File (C#)](Prevent_Admin_from_Checking_In_File_Example_CSharp.htm)
[Prevent Admin from Checking In File (VB.NET)](Prevent_Admin_from_Checking_In_File_Example_VBNET.htm)

## See Also

[EdmSelItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
