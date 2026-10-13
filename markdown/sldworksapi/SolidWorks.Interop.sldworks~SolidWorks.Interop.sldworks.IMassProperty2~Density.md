---
title: "Density Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "Density"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Density.html"
---

# Density Property (IMassProperty2)

Gets the density of selected components/bodies.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Density As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Double

value = instance.Density
```

### C#

```csharp
System.double Density {get;}
```

### C++/CLI

```cpp
property System.double Density {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Density

## VBA Syntax

See [MassProperty2::Density](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~Density.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

If the density varies across components in a model:

Density = ( Mass / Volume )

If [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html) before using this property.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
