---
title: "GetMessageIDs Method (ISwAddinAdvancedOptionBroker)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddinAdvancedOptionBroker"
member: "GetMessageIDs"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker~GetMessageIDs.html"
---

# GetMessageIDs Method (ISwAddinAdvancedOptionBroker)

Gets all of the dismissed messages currently listed on **Tools > Options > System Options > Messages/Errors/Warnings**.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetMessageIDs( _
   ByRef IDs As System.Object, _
   ByRef Message As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddinAdvancedOptionBroker
Dim IDs As System.Object
Dim Message As System.Object

instance.GetMessageIDs(IDs, Message)
```

### C#

```csharp
void GetMessageIDs(
   out System.object IDs,
   out System.object Message
)
```

### C++/CLI

```cpp
void GetMessageIDs(
   [Out] System.Object^ IDs,
   [Out] System.Object^ Message
)
```

### Parameters

- `IDs`: Array of dismissed message IDs
- `Message`: Array of dismissed message strings

## VBA Syntax

See [SwAddinAdvancedOptionBroker::GetMessageIDs](ms-its:swpublishedapivb6.chm::/swpublished~SwAddinAdvancedOptionBroker~GetMessageIDs.html).

## See Also

[ISwAddinAdvancedOptionBroker Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker.html)
[ISwAddinAdvancedOptionBroker Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker_members.html)
[ISwAddinAdvancedOptionBroker::SetMessageIDs Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinAdvancedOptionBroker~SetMessageIDs.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
