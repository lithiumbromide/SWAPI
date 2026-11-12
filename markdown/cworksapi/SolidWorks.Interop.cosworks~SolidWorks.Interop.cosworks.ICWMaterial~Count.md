---
title: "Count Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "Count"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Count.html"
---

# Count Property (ICWMaterial)

Gets the number of properties defined for this material.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Count As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

value = instance.Count
```

### C#

```csharp
System.int Count {get;}
```

### C++/CLI

```cpp
property System.int Count {
   System.int get();
}
```

### Property Value

Number of material properties

## VBA Syntax

See [CWMaterial::Count](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~Count.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetPropertyByName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetPropertyByName.html)
[ICWMaterial::SetPropertyByName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetPropertyByName.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
