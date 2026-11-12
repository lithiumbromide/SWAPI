---
title: "OverrideMomentsOfInertia Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "OverrideMomentsOfInertia"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.html"
---

# OverrideMomentsOfInertia Property (IMassProperty)

Gets or sets whether to override the calculated moments of inertia for the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideMomentsOfInertia As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Boolean

instance.OverrideMomentsOfInertia = value

value = instance.OverrideMomentsOfInertia
```

### C#

```csharp
System.bool OverrideMomentsOfInertia {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideMomentsOfInertia {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the moments of inertia, false to use the calculated values

## VBA Syntax

See [MassProperty::OverrideMomentsOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~OverrideMomentsOfInertia.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverrideMomentsOfInertiaValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMomentsOfInertiaValue.html)
[IMassProperty::SetOverrideMomentsOfInertiaValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMomentsOfInertiaValue.html)
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
