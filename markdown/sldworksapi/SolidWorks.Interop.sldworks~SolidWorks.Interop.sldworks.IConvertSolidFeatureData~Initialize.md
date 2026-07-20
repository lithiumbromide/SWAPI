---
title: "Initialize Method (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "Initialize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~Initialize.html"
---

# Initialize Method (IConvertSolidFeatureData)

Initializes this convert solid feature to have the specified properties.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Initialize( _
   ByVal UseMaterialSheetMetalParameters As System.Boolean, _
   ByVal UseGaugeTableParameters As System.Boolean, _
   ByVal CustomBendAllowance As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim UseMaterialSheetMetalParameters As System.Boolean
Dim UseGaugeTableParameters As System.Boolean
Dim CustomBendAllowance As System.Object

instance.Initialize(UseMaterialSheetMetalParameters, UseGaugeTableParameters, CustomBendAllowance)
```

### C#

```csharp
void Initialize(
   System.bool UseMaterialSheetMetalParameters,
   System.bool UseGaugeTableParameters,
   System.object CustomBendAllowance
)
```

### C++/CLI

```cpp
void Initialize(
   System.bool UseMaterialSheetMetalParameters,
   System.bool UseGaugeTableParameters,
   System.Object^ CustomBendAllowance
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `UseMaterialSheetMetalParameters`: True to use sheet metal parameters attached to the selected material, false to not (see

Remarks

)
- `UseGaugeTableParameters`: True to use a gauge table values (material thickness, bend radius, and bend calculation method) as the basis of this feature, false to not
- `CustomBendAllowance`: [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See

[ConvertSolidFeatureData::Initialize](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~Initialize.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## Remarks

UseMaterialSheetMetalParameters is valid only if a material is applied to the solid.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
