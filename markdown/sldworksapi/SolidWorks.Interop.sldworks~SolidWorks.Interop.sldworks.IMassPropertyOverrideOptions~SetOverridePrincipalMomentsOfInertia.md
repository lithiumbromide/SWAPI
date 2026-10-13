---
title: "SetOverridePrincipalMomentsOfInertia Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "SetOverridePrincipalMomentsOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia.html"
---

# SetOverridePrincipalMomentsOfInertia Method (IMassPropertyOverrideOptions)

Overrides the calculated principal moments of inertia of the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverridePrincipalMomentsOfInertia( _
   ByVal Value As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim Value As System.Object
Dim value As System.Boolean

value = instance.SetOverridePrincipalMomentsOfInertia(Value)
```

### C#

```csharp
System.bool SetOverridePrincipalMomentsOfInertia(
   System.object Value
)
```

### C++/CLI

```cpp
System.bool SetOverridePrincipalMomentsOfInertia(
   System.Object^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Array of three doubles of the principal moments of inertia: **[** Px, Py, Pz **]**

### Return Value

True if the prinicpal moments of inertia are successfully overridden, false if not

## VBA Syntax

See [MassPropertyOverrideOptions::SetOverridePrincipalMomentsOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia.html).

## Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html) is set to true.

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
