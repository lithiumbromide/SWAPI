---
title: "WeldBeadMass Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "WeldBeadMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~WeldBeadMass.html"
---

# WeldBeadMass Property (IMassProperty2)

Gets the weld bead mass.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property WeldBeadMass As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Double

value = instance.WeldBeadMass
```

### C#

```csharp
System.double WeldBeadMass {get;}
```

### C++/CLI

```cpp
property System.double WeldBeadMass {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld bead mass

## VBA Syntax

See [MassProperty2::WeldBeadMass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~WeldBeadMass.html).

## Remarks

This property is valid only if [IMassProperty2::ShowWeldBeadMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~ShowWeldBeadMass.html) is set to true.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
