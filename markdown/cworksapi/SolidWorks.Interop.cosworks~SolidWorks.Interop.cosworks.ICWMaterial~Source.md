---
title: "Source Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "Source"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html"
---

# Source Property (ICWMaterial)

Returns the source of the material.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Source As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

value = instance.Source
```

### C#

```csharp
System.int Source {get;}
```

### C++/CLI

```cpp
property System.int Source {
   System.int get();
}
```

### Property Value

Source of material as defined in [swsMaterialSource_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialSource_e.html)

## VBA Syntax

See [CWMaterial::Source](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~Source.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::Category Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html)
[ICWMaterial::Description Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html)
[ICWMaterial::MaterialName Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html)
[ICWMaterial::MaterialUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
