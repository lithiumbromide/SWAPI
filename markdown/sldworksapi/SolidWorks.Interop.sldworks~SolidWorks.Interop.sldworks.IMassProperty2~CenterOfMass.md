---
title: "CenterOfMass Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "CenterOfMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.html"
---

# CenterOfMass Property (IMassProperty2)

Gets the center of mass of selected components/bodies.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CenterOfMass As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Object

value = instance.CenterOfMass
```

### C#

```csharp
System.object CenterOfMass {get;}
```

### C++/CLI

```cpp
property System.Object^ CenterOfMass {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of three doubles of the x, y, and z coordinates of the center of mass

## VBA Syntax

See [MassProperty2::CenterOfMass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~CenterOfMass.html).

## Remarks

If [IMassPropertyOverrideOptions::OverrideCenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.html) is true or [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html) before using this property.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassPropertyOverrideOptions::SetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.html)
[IMassProeprtyOverrideOptions::GetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideCenterOfMassValue.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
