---
title: "SetOverridePrincipalAxesOrientation Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "SetOverridePrincipalAxesOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.html"
---

# SetOverridePrincipalAxesOrientation Method (IMassPropertyOverrideOptions)

Overrides the orientation of the specified principal axis of inertia of the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverridePrincipalAxesOrientation( _
   ByVal Axis As System.Integer, _
   ByVal Value As System.Object, _
   ByVal AutoCorrect As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim Axis As System.Integer
Dim Value As System.Object
Dim AutoCorrect As System.Boolean
Dim value As System.Boolean

value = instance.SetOverridePrincipalAxesOrientation(Axis, Value, AutoCorrect)
```

### C#

```csharp
System.bool SetOverridePrincipalAxesOrientation(
   System.int Axis,
   System.object Value,
   System.bool AutoCorrect
)
```

### C++/CLI

```cpp
System.bool SetOverridePrincipalAxesOrientation(
   System.int Axis,
   System.Object^ Value,
   System.bool AutoCorrect
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: One of the following principal axes:

  - 0 = X axis
  - 1 = Y axis
  - 2 = Z axis
- `Value`: An array of three doubles of the x, y, and z coordinates of Axis
- `AutoCorrect`: True to generate orthogonal axes, false to not

### Return Value

True if the principal axis orientation successfully overridden, false if not

## VBA Syntax

See [MassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.html).

## Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html) is set to true.

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
