---
title: "GetOverrideMomentsOfInertiaValue Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "GetOverrideMomentsOfInertiaValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue.html"
---

# GetOverrideMomentsOfInertiaValue Method (IMassPropertyOverrideOptions)

Gets the override moments of inertia.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverrideMomentsOfInertiaValue( _
   ByRef IsReferenceFrameSet As System.Boolean, _
   ByRef CoordinateSystemName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim IsReferenceFrameSet As System.Boolean
Dim CoordinateSystemName As System.String
Dim value As System.Object

value = instance.GetOverrideMomentsOfInertiaValue(IsReferenceFrameSet, CoordinateSystemName)
```

### C#

```csharp
System.object GetOverrideMomentsOfInertiaValue(
   out System.bool IsReferenceFrameSet,
   out System.string CoordinateSystemName
)
```

### C++/CLI

```cpp
System.Object^ GetOverrideMomentsOfInertiaValue(
   [Out] System.bool IsReferenceFrameSet,
   [Out] System.String^ CoordinateSystemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IsReferenceFrameSet`: True if reference frame is set, false if not
- `CoordinateSystemName`: Name of coordinate system

### Return Value

Array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

## VBA Syntax

See [MassPropertyOverrideOptions::GetOverrideMomentsOfInertiaValue](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue.html).

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.html)
[IMassPropertyOverrideOptions::OverrideMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html)
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
