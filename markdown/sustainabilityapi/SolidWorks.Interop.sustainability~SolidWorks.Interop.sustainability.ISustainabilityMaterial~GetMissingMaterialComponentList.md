---
title: "GetMissingMaterialComponentList Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "GetMissingMaterialComponentList"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~GetMissingMaterialComponentList.html"
---

# GetMissingMaterialComponentList Method (ISustainabilityMaterial)

Gets the names of the assembly components in the Task List that are missing materials.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMissingMaterialComponentList() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim value As System.Object

value = instance.GetMissingMaterialComponentList()
```

### C#

```csharp
System.object GetMissingMaterialComponentList()
```

### C++/CLI

```cpp
System.Object^ GetMissingMaterialComponentList();
```

### Return Value

Array of names of the assembly components that are missing materials

## VBA Syntax

See [SustainabilityMaterial::GetMissingMaterialComponentList](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~GetMissingMaterialComponentList.html).

## Examples

[Calculate Environmental Impact of Assembly (VBA)](Calculate_Environmental_Impact_of_Assembly_Example_VB.htm)

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::IGetMissingMaterialComponentList Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IGetMissingMaterialComponentList.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
