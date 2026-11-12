---
title: "IncludeComponent Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "IncludeComponent"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IncludeComponent.html"
---

# IncludeComponent Method (ISustainabilityMaterial)

Includes previously excluded assembly components in the calculation of environmental impact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IncludeComponent( _
   ByRef IncludeComponentNames As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim IncludeComponentNames As System.Object

instance.IncludeComponent(IncludeComponentNames)
```

### C#

```csharp
void IncludeComponent(
   ref System.object IncludeComponentNames
)
```

### C++/CLI

```cpp
void IncludeComponent(
   System.Object^% IncludeComponentNames
)
```

### Parameters

- `IncludeComponentNames`: Array of names of previously excluded assembly components to now include in the calculation of environmental impact

## VBA Syntax

See [SustainabilityMaterial::IncludeComponent](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~IncludeComponent.html).

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::IIncludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IIncludeComponent.html)
[ISustainabilityMaterial::ExcludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ExcludeComponent.html)
[ISustainabilityMaterial::IExcludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IExcludeComponent.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
