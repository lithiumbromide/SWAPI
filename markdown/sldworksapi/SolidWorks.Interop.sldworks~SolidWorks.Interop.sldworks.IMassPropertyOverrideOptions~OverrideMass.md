---
title: "OverrideMass Property (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "OverrideMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMass.html"
---

# OverrideMass Property (IMassPropertyOverrideOptions)

Gets or sets whether to override the calculated mass value for the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim value As System.Boolean

instance.OverrideMass = value

value = instance.OverrideMass
```

### C#

```csharp
System.bool OverrideMass {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideMass {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the calculated mass value, false to not

## VBA Syntax

See [MassPropertyOverrideOptions::OverrideMass](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~OverrideMass.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

After setting this property to true, call [IMassPropertyOverrideOptions::SetOverrideMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMassValue.html).

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::Mass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Mass.html)
[IMassPropertyOverrideOptions::GetOverrideMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMassValue.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
