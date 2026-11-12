---
title: "OverrideMomentsOfInertia Property (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "OverrideMomentsOfInertia"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html"
---

# OverrideMomentsOfInertia Property (IMassPropertyOverrideOptions)

Gets or sets whether to override the calculated moments of inertia for the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideMomentsOfInertia As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim value As System.Boolean

instance.OverrideMomentsOfInertia = value

value = instance.OverrideMomentsOfInertia
```

### C#

```csharp
System.bool OverrideMomentsOfInertia {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideMomentsOfInertia {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the calculated moments of inertia, false to not

## VBA Syntax

See [MassPropertyOverrideOptions::OverrideMomentsOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~OverrideMomentsOfInertia.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

After setting this property to true, call:

- [IMassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.html)

- [IMassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.html)

- [IMassPropertyOverrideOptions::SetOverridePrincipalMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia.html)

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.html)
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.html)
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.html)
[IMassPropertyOverrideOptions::GetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue.html)
[IMassPropertyOverrideOptions::GetOverridePrincipalMomentsOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalMomentsOfInertia.html)
[IMassPropertyOverrideOptions::GetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
