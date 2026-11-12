---
title: "SetOverrideCenterOfMassValue Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "SetOverrideCenterOfMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideCenterOfMassValue.html"
---

# SetOverrideCenterOfMassValue Method (IMassPropertyOverrideOptions)

Overrides the calculated center of mass of the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideCenterOfMassValue( _
   ByVal Value As System.Object, _
   ByVal CoordinateSystemName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim Value As System.Object
Dim CoordinateSystemName As System.String
Dim value As System.Boolean

value = instance.SetOverrideCenterOfMassValue(Value, CoordinateSystemName)
```

### C#

```csharp
System.bool SetOverrideCenterOfMassValue(
   System.object Value,
   System.string CoordinateSystemName
)
```

### C++/CLI

```cpp
System.bool SetOverrideCenterOfMassValue(
   System.Object^ Value,
   System.String^ CoordinateSystemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Array of three doubles of the x, y, and z coordinates of the center of mass
- `CoordinateSystemName`: Name of the coordinate system in which the center of mass is defined

### Return Value

True if the center of mass is successfully overridden, false if not

## VBA Syntax

See [MassPropertyOverrideOptions::SetOverrideCenterOfMassValue](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~SetOverrideCenterOfMassValue.html).

## Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideCenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideCenterOfMass.html) is set to true.

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::CenterOfMass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~CenterOfMass.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
