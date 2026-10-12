---
title: "ViewResults Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "ViewResults"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ViewResults.html"
---

# ViewResults Method (ISustainabilityMaterial)

Switches the Sustainability Task Pane from Task List to Assembly Process and calculates the environmental impact of assemblies only.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ViewResults()
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial

instance.ViewResults()
```

### C#

```csharp
void ViewResults()
```

### C++/CLI

```cpp
void ViewResults();
```

## VBA Syntax

See [SustainabilityMaterial::ViewResults](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~ViewResults.html).

## Examples

[Calculate Environmental Impact of Assembly (VBA)](Calculate_Environmental_Impact_of_Assembly_Example_VB.htm)

## Remarks

| Before calling this method, call... | To... |
| --- | --- |
| ISustainabilityMaterial::ExcludeComponent or ISustainabilityMaterial::IExcludeComponent | Exclude components from the environmental impact calculation |
| ISustainabilityMaterial::IncludeComponent or ISustainabilityMaterial::IIncludeComponent | Include components that were previously excluded from the environmental impact calculation |
| ISustainabilityMaterial::GetMissingMaterialComponentList or ISustainabilityMaterial::IGetMissingMaterialComponentList | Get the names of the components that are missing materials |
| ISustainabilityMaterial::MaterialClass | Specify the material class |
| ISustainabilityMaterial::MaterialName | Specify the material name |
| ISustainabilityMaterial::SetPropertiesForComponent or ISustainabilityMaterial::ISetPropertiesForComponent | Set the specified material for the specified components |

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
