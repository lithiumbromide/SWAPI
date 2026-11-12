---
title: "Mass Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "Mass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Mass.html"
---

# Mass Property (IMassProperty2)

Gets the mass of selected components/bodies.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Mass As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Double

value = instance.Mass
```

### C#

```csharp
System.double Mass {get;}
```

### C++/CLI

```cpp
property System.double Mass {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mass

## VBA Syntax

See [MassProperty2::Mass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~Mass.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

If [IMassPropertyOverrideOptions::OverrideMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMass.html) is true or [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html) before using this property.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassPropertyOverrideOptions::SetOverrideMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMassValue.html)
[IMassPropertyOverrideOptions::GetOverrideMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMassValue.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
