---
title: "UseSystemUnits Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "UseSystemUnits"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~UseSystemUnits.html"
---

# UseSystemUnits Property (IMassProperty2)

Gets or sets whether to use system units or document units when calculating mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSystemUnits As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Boolean

instance.UseSystemUnits = value

value = instance.UseSystemUnits
```

### C#

```csharp
System.bool UseSystemUnits {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSystemUnits {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use system units, false to use document units

## VBA Syntax

See [MassProperty2::UseSystemUnits](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~UseSystemUnits.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

The default value is true. Thus, system units (meters, radians, and kilograms) are used by default. All properties returning a value are adjusted accordingly.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
