---
title: "EdmGenItemInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGenItemInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo.html"
---

# EdmGenItemInfo Structure

Contains information about generated items.

## Syntax

### Visual Basic

```vb
Public Structure EdmGenItemInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmGenItemInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmGenItemInfo : public System.ValueType
```

## Examples

struct EdmGenItemInfo{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mlFileID.html);
integer [mlFileParentFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mlFileParentFolderID.html);
string [mbsConfiguration](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mbsConfiguration.html);
integer [mlFileVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mlFileVersion.html);
string [mbsFileFolderPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mbsFileFolderPath.html);
string [mbsFileName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mbsFileName.html);
integer [mlItemID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mlItemID.html);
integer [mlItemParentFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mlItemParentFolderID.html);
[enum EdmItemLinkType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemLinkType.html) [meLinkType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~meLinkType.html);
string [mbsItemFolderPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mbsItemFolderPath.html);
string [mbsItemName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mbsItemName.html);
string [mbsItemAlternativeName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mbsItemAlternativeName.html);
integer [mhResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo~mhResult.html);
};

## Examples

[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)

## Remarks

Returned by [IEdmBatchItemGeneration::GenerateItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~GenerateItems.html).

## See Also

[EdmGenItemInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
