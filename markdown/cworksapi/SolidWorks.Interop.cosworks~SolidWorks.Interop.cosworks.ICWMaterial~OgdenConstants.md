---
title: "OgdenConstants Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "OgdenConstants"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~OgdenConstants.html"
---

# OgdenConstants Property (ICWMaterial)

Gets or sets the Ogden constants used for the Ogden material model used for nonlinear studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property OgdenConstants As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.OgdenConstants = value

value = instance.OgdenConstants
```

### C#

```csharp
System.int OgdenConstants {get; set;}
```

### C++/CLI

```cpp
property System.int OgdenConstants {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of Ogden constants

## VBA Syntax

See [CWMaterial::OgdenConstants](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~OgdenConstants.html).

## Remarks

Ogden constants are valid in nonlinear studies only.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
