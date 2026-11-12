---
title: "GetOverridePrincipalMomentsOfInertia Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "GetOverridePrincipalMomentsOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalMomentsOfInertia.html"
---

# GetOverridePrincipalMomentsOfInertia Method (IMassPropertyOverrideOptions)

Gets the override principal moments of inertia.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverridePrincipalMomentsOfInertia() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim value As System.Object

value = instance.GetOverridePrincipalMomentsOfInertia()
```

### C#

```csharp
System.object GetOverridePrincipalMomentsOfInertia()
```

### C++/CLI

```cpp
System.Object^ GetOverridePrincipalMomentsOfInertia();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of three doubles of the principal moments of inertia: **[** Px, Py, Pz **]**

## VBA Syntax

See [MassPropertyOverrideOptions::GetOverridePrincipalMomentsOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~GetOverridePrincipalMomentsOfInertia.html).

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassPropertyOverrideOptions::SetOverridePrincipalMomentsOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalMomentsOfInertia.html)
[IMassPropertyOverrideOptions::OverrideMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html)
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
