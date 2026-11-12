---
title: "SetOverrideMomentsOfInertiaValue Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "SetOverrideMomentsOfInertiaValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.html"
---

# SetOverrideMomentsOfInertiaValue Method (IMassPropertyOverrideOptions)

Overrides the calculated moments of inertia of the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideMomentsOfInertiaValue( _
   ByVal ReferenceFrame As System.Integer, _
   ByVal Value As System.Object, _
   ByVal CoordinateSystemName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim ReferenceFrame As System.Integer
Dim Value As System.Object
Dim CoordinateSystemName As System.String
Dim value As System.Boolean

value = instance.SetOverrideMomentsOfInertiaValue(ReferenceFrame, Value, CoordinateSystemName)
```

### C#

```csharp
System.bool SetOverrideMomentsOfInertiaValue(
   System.int ReferenceFrame,
   System.object Value,
   System.string CoordinateSystemName
)
```

### C++/CLI

```cpp
System.bool SetOverrideMomentsOfInertiaValue(
   System.int ReferenceFrame,
   System.Object^ Value,
   System.String^ CoordinateSystemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferenceFrame`: Frame of reference as defined in [swMomentsOfInertiaReferenceFrame_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMomentsOfInertiaReferenceFrame_e.html)
- `Value`: Array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]
- `CoordinateSystemName`: Name of coordinate system; valid only if ReferenceFrame = swMomentsOfInertiaReferenceFrame_e.swMomentsOfInertiaReferenceFrame_UserCoordinateSystem

### Return Value

True if the moments of inertia are successfully overridden, false if not

## VBA Syntax

See [MassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html) is set to true.

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
