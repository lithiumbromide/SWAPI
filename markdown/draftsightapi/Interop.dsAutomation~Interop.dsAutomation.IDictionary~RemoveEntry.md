---
title: "RemoveEntry Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "RemoveEntry"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html"
---

# RemoveEntry Method (IDictionary)

Removes the entity with the specified name from the dictionary.

## Syntax

### Visual Basic

```vb
Sub RemoveEntry( _
   ByVal Name As System.String _
)
```

### C#

```csharp
void RemoveEntry(
   System.string Name
)
```

### JScript

```
function RemoveEntry(
   Name : System.String
);
```

### Managed Extensions for C++

```
void RemoveEntry(
   System.string* Name
)
```

### C++/CLI

```cpp
void RemoveEntry(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the entity to remove from the dictionary

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)
[Create and Remove Dictionary (JavaScript)](Create_and_Remove_Dictionary_Example_JS.htm)

## Remarks

Only the entity that matches the specified name in this dictionary is removed. If the entity exists in the drawing, then the entity is not removed from the drawing.

**NOTE**: You can also remove dictionaries or XRecords in a dictionary using [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html) or [IXRecord::Erased](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html), respectively. However, IXDictionary::Erased and IXRecord::Erased require you to call [IDictionary::SetEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html) to restore any dictionaries or XRecords erased using IDictionary::Erased or IXRecord::Erased. If you removed any dictionaries or XRecords using IDictionary::RemoveEntry, then you do not have to call IDictionary::SetEntry to restore the removed dictionaries or XRecords.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntries Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html)
[IDictionary::GetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html)
[IDictionary::GetNameOf Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html)
[IDictionary::HasEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html)
[IDictionary::RenameEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html)

## Availability

DraftSight V1R4.0
