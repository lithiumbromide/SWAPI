---
title: "Action Property (IVersionCompatibilityItem)"
project: "SOLIDWORKS API Help"
interface: "IVersionCompatibilityItem"
member: "Action"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem~Action.html"
---

# Action Property (IVersionCompatibilityItem)

Gets the localized message describing he corrective action recommended for this incompatibility.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Action As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IVersionCompatibilityItem
Dim value As System.String

value = instance.Action
```

### C#

```csharp
System.string Action {get;}
```

### C++/CLI

```cpp
property System.String^ Action {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [VersionCompatibilityItem::Action](ms-its:sldworksapivb6.chm::/sldworks~VersionCompatibilityItem~Action.html).

## See Also

[IVersionCompatibilityItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem.html)
[IVersionCompatibilityItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem_members.html)

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
