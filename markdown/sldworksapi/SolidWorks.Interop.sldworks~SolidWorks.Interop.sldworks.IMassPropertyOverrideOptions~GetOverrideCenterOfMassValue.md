---
title: "GetOverrideCenterOfMassValue Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "GetOverrideCenterOfMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideCenterOfMassValue.html"
---

# GetOverrideCenterOfMassValue Method (IMassPropertyOverrideOptions)

Gets the override center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverrideCenterOfMassValue( _
   ByRef CoordinateSystemName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim CoordinateSystemName As System.String
Dim value As System.Object

value = instance.GetOverrideCenterOfMassValue(CoordinateSystemName)
```

### C#

```csharp
System.object GetOverrideCenterOfMassValue(
   out System.string CoordinateSystemName
)
```

### C++/CLI

```cpp
System.Object^ GetOverrideCenterOfMassValue(
   [Out] System.String^ CoordinateSystemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CoordinateSystemName`: Name of the coordinate system in which the center of mass is defined

### Return Value

Array of three doubles of the x, y, and z coordinates of the center of mass

## VBA Syntax

See [MassPropertyOverrideOptions::GetOverrideCenterOfMassValue](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~GetOverrideCenterOfMassValue.html).

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassPropertyOverrideOptions::SetOverrideCenterOfMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.html)
[IMassProperty2::CenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.html)
[IMassPropertyOverrideOptions::OverrideCenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
