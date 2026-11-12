---
title: "GetReferencePlaneName Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetReferencePlaneName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetReferencePlaneName.html"
---

# GetReferencePlaneName Method (ICWMaterial)

Gets the name of the reference plane or reference axis used to specify material properties for orthotropic materials.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencePlaneName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.String

value = instance.GetReferencePlaneName()
```

### C#

```csharp
System.string GetReferencePlaneName()
```

### C++/CLI

```cpp
System.String^ GetReferencePlaneName();
```

### Return Value

Name of reference plane or reference geometry

## VBA Syntax

See [CWMaterial::GetReferencePlaneName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetReferencePlaneName.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::SetReferencePlane Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetReferencePlane.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
