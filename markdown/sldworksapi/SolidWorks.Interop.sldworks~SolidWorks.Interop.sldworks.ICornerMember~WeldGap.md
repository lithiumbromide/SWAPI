---
title: "WeldGap Property (ICornerMember)"
project: "SOLIDWORKS API Help"
interface: "ICornerMember"
member: "WeldGap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~WeldGap.html"
---

# WeldGap Property (ICornerMember)

Gets and sets the weld gap of this corner member.

## Syntax

### Visual Basic (Declaration)

```vb
Property WeldGap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerMember
Dim value As System.Double

instance.WeldGap = value

value = instance.WeldGap
```

### C#

```csharp
System.double WeldGap {get; set;}
```

### C++/CLI

```cpp
property System.double WeldGap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld gap in meters between members; default is 0.0

## VBA Syntax

See [CornerMember::WeldGap](ms-its:sldworksapivb6.chm::/sldworks~CornerMember~WeldGap.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html)
[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
