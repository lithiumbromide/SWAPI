---
title: "IGetMissingMaterialComponentList Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "IGetMissingMaterialComponentList"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IGetMissingMaterialComponentList.html"
---

# IGetMissingMaterialComponentList Method (ISustainabilityMaterial)

Gets the names of the assembly components that are missing materials.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetMissingMaterialComponentList( _
   ByVal Count As System.Integer, _
   ByRef ComponentsNames As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim Count As System.Integer
Dim ComponentsNames As System.String

instance.IGetMissingMaterialComponentList(Count, ComponentsNames)
```

### C#

```csharp
void IGetMissingMaterialComponentList(
   System.int Count,
   ref System.string ComponentsNames
)
```

### C++/CLI

```cpp
void IGetMissingMaterialComponentList(
   System.int Count,
   System.String^% ComponentsNames
)
```

### Parameters

- `Count`: Number of assembly components returned in ComponentsNames (see **Remarks**)
- `ComponentsNames`: - in-process, unmanaged C++: Pointer to an array of the names of the assembly components that are missing materials
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISustainabilityMaterial::GetMissingMaterialComponentCount](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~GetMissingMaterialComponentCount.html) to assign Count.

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::GetMissingMaterialComponentList Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~GetMissingMaterialComponentList.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
