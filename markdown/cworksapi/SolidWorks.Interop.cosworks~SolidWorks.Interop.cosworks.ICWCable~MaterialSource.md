---
title: "MaterialSource Property (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "MaterialSource"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~MaterialSource.html"
---

# MaterialSource Property (ICWCable)

Sets the material source of this cable.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property MaterialSource As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable

instance.MaterialSource = value
```

### C#

```csharp
System.int MaterialSource {set;}
```

### C++/CLI

```cpp
property System.int MaterialSource {
   void set (    System.int value);
}
```

### Property Value

Material source as defined by swsBoltMaterialSource_e:

0 = From SOLIDWORKS

1 = Custom defined

2 = From library files

## VBA Syntax

See [CWCable::MaterialSource](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~MaterialSource.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## Remarks

If this property is set to custom defined, then you must set ICWCable::ShearModulus, ThermalCoefficient, or YoungsModulus.

| If this property is set to... | Then set ... |
| --- | --- |
| Custom | ICWCable::ShearModulus , ICWCable::ThermalCoefficient , or ICWCable::YoungsModulus |
| Library | ICWCable::SetLibraryMaterial |

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
