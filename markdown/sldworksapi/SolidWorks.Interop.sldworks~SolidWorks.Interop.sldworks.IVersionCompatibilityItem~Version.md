---
title: "Version Property (IVersionCompatibilityItem)"
project: "SOLIDWORKS API Help"
interface: "IVersionCompatibilityItem"
member: "Version"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem~Version.html"
---

# Version Property (IVersionCompatibilityItem)

Gets the name of the version of SOLIDWORKS to which this incompatibility relates.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Version As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IVersionCompatibilityItem
Dim value As System.String

value = instance.Version
```

### C#

```csharp
System.string Version {get;}
```

### C++/CLI

```cpp
property System.String^ Version {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [VersionCompatibilityItem::Version](ms-its:sldworksapivb6.chm::/sldworks~VersionCompatibilityItem~Version.html).

## Remarks

The string returned is the year element of the SOLIDWORKS version name. I.e. "2024" or "2025" or "2026", etc.

## See Also

[IVersionCompatibilityItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem.html)
[IVersionCompatibilityItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem_members.html)

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
