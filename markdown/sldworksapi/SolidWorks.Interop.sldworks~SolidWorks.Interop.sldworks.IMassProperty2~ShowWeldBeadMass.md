---
title: "ShowWeldBeadMass Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "ShowWeldBeadMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~ShowWeldBeadMass.html"
---

# ShowWeldBeadMass Property (IMassProperty2)

Gets or sets whether to calculate weld bead mass.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowWeldBeadMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Boolean

instance.ShowWeldBeadMass = value

value = instance.ShowWeldBeadMass
```

### C#

```csharp
System.bool ShowWeldBeadMass {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowWeldBeadMass {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to calculate weld bead mass, false to not

## VBA Syntax

See [MassProperty2::ShowWeldBeadMass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~ShowWeldBeadMass.html).

## Remarks

After setting this property to true, you can use [IMassProperty2::WeldBeadMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~WeldBeadMass.html).

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
