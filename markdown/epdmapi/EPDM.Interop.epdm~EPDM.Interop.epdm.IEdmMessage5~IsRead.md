---
title: "IsRead Property (IEdmMessage5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMessage5"
member: "IsRead"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5~IsRead.html"
---

# IsRead Property (IEdmMessage5)

Gets or sets whether the message has been read.

## Syntax

### Visual Basic

```vb
Property IsRead As System.Boolean
```

### C#

```csharp
System.bool IsRead {get; set;}
```

### C++/CLI

```cpp
property System.bool IsRead {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the message has been read, false if not (see **Remarks**)

## Examples

See the [IEdmMessage5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5.html) examples.

## Remarks

You can only set this property to true; you cannot set it to false.

## See Also

[IEdmMessage5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5.html)
[IEdmMessage5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5_members.html)

## Availability

Version 5.3 of SOLIDWORKS PDM Professional
