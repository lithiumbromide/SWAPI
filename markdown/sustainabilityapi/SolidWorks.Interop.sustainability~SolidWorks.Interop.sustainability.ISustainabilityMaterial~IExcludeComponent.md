---
title: "IExcludeComponent Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "IExcludeComponent"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IExcludeComponent.html"
---

# IExcludeComponent Method (ISustainabilityMaterial)

Excludes the specified assembly components from the calculation of environmental impact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IExcludeComponent( _
   ByVal Count As System.Integer, _
   ByRef ExcludeComponentNames As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim Count As System.Integer
Dim ExcludeComponentNames As System.String

instance.IExcludeComponent(Count, ExcludeComponentNames)
```

### C#

```csharp
void IExcludeComponent(
   System.int Count,
   ref System.string ExcludeComponentNames
)
```

### C++/CLI

```cpp
void IExcludeComponent(
   System.int Count,
   System.String^% ExcludeComponentNames
)
```

### Parameters

- `Count`: Number of assembly components in ExcludeComponentNames
- `ExcludeComponentNames`: - in-process, unmanaged C++: Pointer to an array of the names of the assembly components to exclude from the calculation of environmental impact
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::ExcludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ExcludeComponent.html)
[ISustainabilityMaterial::IIncludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IIncludeComponent.html)
[ISustainabilityMaterial::IncludeComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~IncludeComponent.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
