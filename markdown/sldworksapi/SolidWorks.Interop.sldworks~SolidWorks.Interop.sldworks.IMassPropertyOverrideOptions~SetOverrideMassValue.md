---
title: "SetOverrideMassValue Method (IMassPropertyOverrideOptions)"
project: "SOLIDWORKS API Help"
interface: "IMassPropertyOverrideOptions"
member: "SetOverrideMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMassValue.html"
---

# SetOverrideMassValue Method (IMassPropertyOverrideOptions)

Overrides the calculated mass of the model currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideMassValue( _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassPropertyOverrideOptions
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetOverrideMassValue(Value)
```

### C#

```csharp
System.bool SetOverrideMassValue(
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetOverrideMassValue(
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: New mass value

### Return Value

True if the mass is successfully overridden, false if not

## VBA Syntax

See [MassPropertyOverrideOptions::SetOverrideMassValue](ms-its:sldworksapivb6.chm::/sldworks~MassPropertyOverrideOptions~SetOverrideMassValue.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMass.html) is set to true.

## See Also

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html)
[IMassProperty2::Mass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Mass.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
