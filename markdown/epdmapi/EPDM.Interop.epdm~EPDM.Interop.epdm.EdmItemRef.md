---
title: "EdmItemRef Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmItemRef"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html"
---

# EdmItemRef Structure

Contains information about an item reference.

## Syntax

### Visual Basic

```vb
Public Structure EdmItemRef
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmItemRef : System.ValueType
```

### C++/CLI

```cpp
public value class EdmItemRef : public System.ValueType
```

## Examples

struct EdmItemRef

{
integer [mlEdmRefFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef~mlEdmRefFlags.html);
string [mbsConfiguration](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef~mbsConfiguration.html);
object [moNamePathOrID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef~moNamePathOrID.html);
object [moParentNamePathOrItemID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef~moParentNamePathOrItemID.html);
integer [mhResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef~mhResult.html);
};

## Examples

[Batch Add Item References (VB.NET)](Batch_Add_and_Remove_Item_References_Example_VBNET.htm)
[Batch Add Item References (C#)](Batch_Add_and_Remove_Item_References_Example_CSharp.htm)
[Get and Set Item References (VB.NET)](Get_and_Set_Item_References_Example_VBNET.htm)
[Get and Set Item References (C#)](Get_and_Set_Item_References_Example_CSharp.htm)

## Remarks

Used by [IEdmItem::GetReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~GetReferences.html), [IEdmItem::UpdateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~UpdateReferences.html), and [IEdmBatchItemReferenceUpdate::UpdateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate~UpdateReferences.html).

## See Also

[EdmItemRef Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
