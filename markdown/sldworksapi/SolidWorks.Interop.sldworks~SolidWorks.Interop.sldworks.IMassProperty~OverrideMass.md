---
title: "OverrideMass Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "OverrideMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMass.html"
---

# OverrideMass Property (IMassProperty)

Gets or sets whether to override the calculated mass value for the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Boolean

instance.OverrideMass = value

value = instance.OverrideMass
```

### C#

```csharp
System.bool OverrideMass {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideMass {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the mass value, false to use the calculated value

## VBA Syntax

See [MassProperty::OverrideMass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~OverrideMass.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverrideMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMassValue.html)
[IMassProperty::SetOverrideMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMassValue.html)
[IMassProperty::Mass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Mass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
