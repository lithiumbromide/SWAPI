---
title: "IIncludeComponent Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "IIncludeComponent"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IIncludeComponent.html"
---

# IIncludeComponent Method (ISustainabilityMaterial)

Includes previously excluded assembly components in the calculation of environmental impact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IIncludeComponent( _
   ByVal Count As System.Integer, _
   ByRef IncludeComponentNames As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim Count As System.Integer
Dim IncludeComponentNames As System.String

instance.IIncludeComponent(Count, IncludeComponentNames)
```

### C#

```csharp
void IIncludeComponent(
   System.int Count,
   ref System.string IncludeComponentNames
)
```

### C++/CLI

```cpp
void IIncludeComponent(
   System.int Count,
   System.String^% IncludeComponentNames
)
```

### Parameters

- `Count`: Number of assembly components in IncludeComponentNames
- `IncludeComponentNames`: - in-process, unmanaged C++: Pointer to an array of the names of previously excluded assembly components to now include in the calculation of environmental impact
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::IncludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IncludeComponent.html)
[ISustainabilityMaterial::IExcludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IExcludeComponent.html)
[ISustainabilityMaterial::ExcludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ExcludeComponent.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
