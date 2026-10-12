---
title: "ExcludeComponent Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "ExcludeComponent"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ExcludeComponent.html"
---

# ExcludeComponent Method (ISustainabilityMaterial)

Excludes the specified assembly components from the calculation of environmental impact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ExcludeComponent( _
   ByRef ExcludeComponentNames As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim ExcludeComponentNames As System.Object

instance.ExcludeComponent(ExcludeComponentNames)
```

### C#

```csharp
void ExcludeComponent(
   ref System.object ExcludeComponentNames
)
```

### C++/CLI

```cpp
void ExcludeComponent(
   System.Object^% ExcludeComponentNames
)
```

### Parameters

- `ExcludeComponentNames`: Array of the names of the assembly components to exclude from the calculation of environmental impact

## VBA Syntax

See [SustainabilityMaterial::ExcludeComponent](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~ExcludeComponent.html).

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::IExcludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IExcludeComponent.html)
[ISustainabilityMaterial::IIncludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IIncludeComponent.html)
[ISustainabilityMaterial::IncludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IncludeComponent.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
