---
title: "SenderName Property (IEdmMessage5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMessage5"
member: "SenderName"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5~SenderName.html"
---

# SenderName Property (IEdmMessage5)

Gets the name of the user who sent the message.

## Syntax

### Visual Basic

```vb
ReadOnly Property SenderName As System.String
```

### C#

```csharp
System.string SenderName {get;}
```

### C++/CLI

```cpp
property System.String^ SenderName {
   System.String^ get();
}
```

### Property Value

Name of the user who sent the message; an empty string indicates that the message was a notification

## Examples

See the [IEdmMessage5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5.html) examples.

## See Also

[IEdmMessage5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5.html)
[IEdmMessage5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5_members.html)

## Availability

Version 5.3 of SOLIDWORKS PDM Professional
