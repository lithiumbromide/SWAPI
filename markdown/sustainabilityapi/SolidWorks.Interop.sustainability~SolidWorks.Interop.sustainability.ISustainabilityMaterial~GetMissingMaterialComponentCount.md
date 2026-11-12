---
title: "GetMissingMaterialComponentCount Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "GetMissingMaterialComponentCount"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~GetMissingMaterialComponentCount.html"
---

# GetMissingMaterialComponentCount Method (ISustainabilityMaterial)

Gets the number of assembly components in the Task List that are missing materials.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMissingMaterialComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim value As System.Integer

value = instance.GetMissingMaterialComponentCount()
```

### C#

```csharp
System.int GetMissingMaterialComponentCount()
```

### C++/CLI

```cpp
System.int GetMissingMaterialComponentCount();
```

### Return Value

Number of assembly components missing materials

## VBA Syntax

See [SustainabilityMaterial::GetMissingMaterialComponentCount](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~GetMissingMaterialComponentCount.html).

## Examples

[Calculate Environmental Impact of Assembly (VBA)](Calculate_Environmental_Impact_of_Assembly_Example_VB.htm)

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::GetMissingMaterialComponentList Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~GetMissingMaterialComponentList.html)
[ISustainabilityMaterial::IGetMissingMaterialComponentList Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IGetMissingMaterialComponentList.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
