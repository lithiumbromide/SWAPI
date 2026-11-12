---
title: "GetOverridePrincipalAxesOrientation Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "GetOverridePrincipalAxesOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation.html"
---

# GetOverridePrincipalAxesOrientation Method (IMassPropertyOverrideOptions)

Gets the override principal axis of inertia.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverridePrincipalAxesOrientation( _
   ByVal Axis As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim Axis As System.Integer
Dim value As System.Object

value = instance.GetOverridePrincipalAxesOrientation(Axis)
```

### C#

```csharp
System.object GetOverridePrincipalAxesOrientation(
   System.int Axis
)
```

### C++/CLI

```cpp
System.Object^ GetOverridePrincipalAxesOrientation(
   System.int Axis
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: One of the following principal axes:

  - 0 = X axis
  - 1 = Y axis
  - 2 = Z axis

### Return Value

An array of three doubles of the x, y, and z coordinates of Axis

## VBA Syntax

See [MassPropertyOverrideOptions::GetOverridePrincipalAxesOrientation](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation.html).

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.html)
[IMassPropertyOverrideOptions::OverrideMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html)
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
