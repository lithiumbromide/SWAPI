---
title: "CreateXRecord Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "CreateXRecord"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateXRecord.html"
---

# CreateXRecord Method (IDictionary)

Creates the specified record in the specified dictionary.

## Syntax

### Visual Basic

```vb
Function CreateXRecord( _
   ByVal Name As System.String _
) As XRecord
```

### C#

```csharp
XRecord CreateXRecord(
   System.string Name
)
```

### JScript

```
function CreateXRecord(
   Name : System.String
) : XRecord;
```

### Managed Extensions for C++

```
XRecord* CreateXRecord(
   System.string* Name
)
```

### C++/CLI

```cpp
XRecord^ CreateXRecord(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the record to create in the dictionary

### Return Value

[Record](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html) in the dictionary (see **Remarks**)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)
[Create and Remove Dictionary (JavaScript)](Create_and_Remove_Dictionary_Example_JS.htm)

## Remarks

If the specified record already exists in the dictionary, then it is not overwritten.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)

## Availability

DraftSight V1R4.0
