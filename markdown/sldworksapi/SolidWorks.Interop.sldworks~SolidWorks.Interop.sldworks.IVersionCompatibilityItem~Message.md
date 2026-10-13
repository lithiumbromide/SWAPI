---
title: "Message Property (IVersionCompatibilityItem)"
project: "SOLIDWORKS API Help"
interface: "IVersionCompatibilityItem"
member: "Message"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem~Message.html"
---

# Message Property (IVersionCompatibilityItem)

Gets the localized message describing this incompatibility.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Message As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IVersionCompatibilityItem
Dim value As System.String

value = instance.Message
```

### C#

```csharp
System.string Message {get;}
```

### C++/CLI

```cpp
property System.String^ Message {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [VersionCompatibilityItem::Message](ms-its:sldworksapivb6.chm::/sldworks~VersionCompatibilityItem~Message.html).

## See Also

[IVersionCompatibilityItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem.html)
[IVersionCompatibilityItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem_members.html)

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
