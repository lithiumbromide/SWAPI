---
title: "IsAligned Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IsAligned"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IsAligned.html"
---

# IsAligned Method (IDrSection)

Gets whether this is an aligned section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsAligned() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.IsAligned()
```

### C#

```csharp
System.bool IsAligned()
```

### C++/CLI

```cpp
System.bool IsAligned();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this is an aligned section view, false if it is not

## VBA Syntax

See [DrSection::IsAligned](ms-its:sldworksapivb6.chm::/sldworks~DrSection~IsAligned.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
