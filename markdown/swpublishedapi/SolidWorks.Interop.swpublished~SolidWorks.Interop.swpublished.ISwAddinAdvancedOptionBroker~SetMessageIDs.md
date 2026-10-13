---
title: "SetMessageIDs Method (ISwAddinAdvancedOptionBroker)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddinAdvancedOptionBroker"
member: "SetMessageIDs"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker~SetMessageIDs.html"
---

# SetMessageIDs Method (ISwAddinAdvancedOptionBroker)

Sets the specified dismissed messages to display on **Tools > Options > System Options > Messages/Errors/Warnings**.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMessageIDs( _
   ByVal IDs As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddinAdvancedOptionBroker
Dim IDs As System.Object

instance.SetMessageIDs(IDs)
```

### C#

```csharp
void SetMessageIDs(
   System.object IDs
)
```

### C++/CLI

```cpp
void SetMessageIDs(
   System.Object^ IDs
)
```

### Parameters

- `IDs`: Array of IDs of dismissed messages to display (see **Remarks**)

## VBA Syntax

See [SwAddinAdvancedOptionBroker::SetMessageIDs](ms-its:swpublishedapivb6.chm::/swpublished~SwAddinAdvancedOptionBroker~SetMessageIDs.html).

## Remarks

By omission, this method effectively removes one or more dismissed messages from the list on **Tools > Options > System Options > Messages/Errors/Warnings**.

Before calling this method use [ISwAddinAdvancedOptionBroker::GetMessageIDs](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddinAdvancedOptionBroker~GetMessageIDs.html) to obtain the IDs of the current list of dismissed messages.

## See Also

[ISwAddinAdvancedOptionBroker Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker.html)
[ISwAddinAdvancedOptionBroker Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
