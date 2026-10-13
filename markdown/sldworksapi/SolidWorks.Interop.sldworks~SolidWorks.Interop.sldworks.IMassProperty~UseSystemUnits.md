---
title: "UseSystemUnits Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "UseSystemUnits"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UseSystemUnits.html"
---

# UseSystemUnits Property (IMassProperty)

Gets and sets whether to use system units or document units when calculating mass properties for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSystemUnits As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
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

See [MassProperty::UseSystemUnits](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~UseSystemUnits.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Propeties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Propeties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## Remarks

The default value is True. Thus, system units (meters, radians, and kilograms) are used. All properties returning a value are adjusted accordingly.

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
