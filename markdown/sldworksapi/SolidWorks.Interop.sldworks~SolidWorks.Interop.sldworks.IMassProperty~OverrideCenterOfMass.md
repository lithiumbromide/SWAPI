---
title: "OverrideCenterOfMass Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "OverrideCenterOfMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.html"
---

# OverrideCenterOfMass Property (IMassProperty)

Gets or sets whether to override the calculated center of mass value for the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideCenterOfMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Boolean

instance.OverrideCenterOfMass = value

value = instance.OverrideCenterOfMass
```

### C#

```csharp
System.bool OverrideCenterOfMass {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideCenterOfMass {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the center of mass value, false to use the calculated value

## VBA Syntax

See [MassProperty::OverrideCenterOfMass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~OverrideCenterOfMass.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue.html)
[IMassProperty::SetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue.html)
[IMassProperty::CenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
