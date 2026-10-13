---
title: "GetControlVariableList Method (IEdmCardControl7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl7"
member: "GetControlVariableList"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7~GetControlVariableList.html"
---

# GetControlVariableList Method (IEdmCardControl7)

Gets the list values associated with this drop-down list card control.

## Syntax

### Visual Basic

```vb
Function GetControlVariableList( _
   ByVal lDocumentId As System.Integer, _
   ByRef ppVariableItemsList As System.String() _
) As System.Boolean
```

### C#

```csharp
System.bool GetControlVariableList(
   System.int lDocumentId,
   out System.string[] ppVariableItemsList
)
```

### C++/CLI

```cpp
System.bool GetControlVariableList(
   System.int lDocumentId,
   [Out] System.array<String^> ppVariableItemsList
)
```

### Parameters

- `lDocumentId`: ID of the file
- `ppVariableItemsList`: Array of list values; empty if the card control is not associated with a list (see **Remarks**)

### Return Value

True if retrieving the list is successful, false if not

## Examples

See the [IEdmCardControl7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7.html) examples.

## Remarks

This method is valid only if [IEdmCardControl5::ControlType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~ControlType.html) is set to [EdmCardControlType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardControlType.html):

- EdmCtrl_ComboboxDropdown
- EdmCtrl_ComboboxDroplist
- EdmCtrl_ComboboxSimple
- EdmCtrl_Listbox

This method supports the following items that appear in the **Admin tool > Card Editor** when you double-click on a droplist, dropdown, or listbox card control:

- Free text
- Controlled by variable
- Special value > User list or Group list

This method does not support add-in lists.

## See Also

[IEdmCardControl7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7.html)
[IEdmCardControl7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
