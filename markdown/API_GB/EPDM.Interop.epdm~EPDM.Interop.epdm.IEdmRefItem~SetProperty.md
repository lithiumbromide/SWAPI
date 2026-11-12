---
title: "SetProperty Method (IEdmRefItem)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRefItem"
member: "SetProperty"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem~SetProperty.html"
---

# SetProperty Method (IEdmRefItem)

Updates the specified property of this item.

## Syntax

### Visual Basic

```vb
Sub SetProperty( _
   ByVal eProperty As EdmRefItemProperty, _
   ByVal oValue As System.Object _
)
```

### C#

```csharp
void SetProperty(
   EdmRefItemProperty eProperty,
   System.object oValue
)
```

### C++/CLI

```cpp
void SetProperty(
   EdmRefItemProperty eProperty,
   System.Object^ oValue
)
```

### Parameters

- `eProperty`: Type of property to update as defined in [EdmRefItemProperty](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefItemProperty.html)
- `oValue`: New property value

## Examples

[Access Check-in Flags in Check out Dialog (C#)](Access_Check-in_Flags_in_Check_in_Dialog_Example_CSharp.htm)
[Access Check-in Flags in Check out Dialog (VB.NET)](Access_Check-in_Flags_in_Check_in_Dialog_Example_VBNET.htm)
[Prevent Admin from Checking In File (C#)](Prevent_Admin_from_Checking_In_File_Example_CSharp.htm)
[Prevent Admin from Checking In File (VB.NET)](Prevent_Admin_from_Checking_In_File_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_INVALIDARG: The eProperty argument contains a property that cannot be updated in this container, or oValue does not match the type specified in eProperty.

## See Also

[IEdmRefItem Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)
[IEdmRefItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
