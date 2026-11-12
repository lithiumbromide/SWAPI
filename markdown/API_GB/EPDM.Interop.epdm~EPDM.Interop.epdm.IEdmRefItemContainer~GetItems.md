---
title: "GetItems Method (IEdmRefItemContainer)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRefItemContainer"
member: "GetItems"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer~GetItems.html"
---

# GetItems Method (IEdmRefItemContainer)

Gets items from this container.

## Syntax

### Visual Basic

```vb
Sub GetItems( _
   ByVal eType As EdmRefItemType, _
   ByRef ppoRetItems As System.Object() _
)
```

### C#

```csharp
void GetItems(
   EdmRefItemType eType,
   out System.object[] ppoRetItems
)
```

### C++/CLI

```cpp
void GetItems(
   EdmRefItemType eType,
   [Out] System.array<Object^> ppoRetItems
)
```

### Parameters

- `eType`: Type of items to get as defined in [EdmRefItemType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefItemType.html)
- `ppoRetItems`: Array of [IEdmRefItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)s; one interface for each reference item

## Examples

[Access Check-in Flags in Check out Dialog (C#)](Access_Check-in_Flags_in_Check_in_Dialog_Example_CSharp.htm)
[Access Check-in Flags in Check out Dialog (VB.NET)](Access_Check-in_Flags_in_Check_in_Dialog_Example_VBNET.htm)
[Prevent Admin from Checking In File (C#)](Prevent_Admin_from_Checking_In_File_Example_CSharp.htm)
[Prevent Admin from Checking In File (VB.NET)](Prevent_Admin_from_Checking_In_File_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRefItemContainer Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer.html)
[IEdmRefItemContainer Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
