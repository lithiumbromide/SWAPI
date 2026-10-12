---
title: "OverrideCenterOfMass Property (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "OverrideCenterOfMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.html"
---

# OverrideCenterOfMass Property (IMassPropertyOverrideOptions)

Gets or sets whether to override the calculated center of mass for the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideCenterOfMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim value As System.Boolean

instance.OverrideCenterOfMass = value

value = instance.OverrideCenterOfMass
```

### C#

```csharp
System.bool OverrideCenterOfMass {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideCenterOfMass {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the calculated center of mass, false to not

## VBA Syntax

See [MassPropertyOverrideOptions::OverrideCenterOfMass](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~OverrideCenterOfMass.html).

## Remarks

After setting this property to true, call [IMassPropertyOverrideOptions::SetOverrideCenterOfMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.html).

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::CenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.html)
[IMassPropertyOverrideOptions::GetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideCenterOfMassValue.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
