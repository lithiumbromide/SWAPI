---
title: "OverrideDefaultSheetMetalParameters Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "OverrideDefaultSheetMetalParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultSheetMetalParameters.html"
---

# OverrideDefaultSheetMetalParameters Property (IConvertSolidFeatureData)

Gets or sets whether to override the default sheet metal parameters such as sheet thickness and default bend radius for this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDefaultSheetMetalParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.OverrideDefaultSheetMetalParameters = value

value = instance.OverrideDefaultSheetMetalParameters
```

### C#

```csharp
System.bool OverrideDefaultSheetMetalParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDefaultSheetMetalParameters {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to override the default sheet metal parameters, false to not

## VBA Syntax

See

[ConvertSolidFeatureData::OverrideDefaultSheetMetalParameters](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~OverrideDefaultSheetMetalParameters.html)

.

## Remarks

If this property is set to true, you can set:

- [IConvertSolidFeatureData::SheetThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~SheetThickness.html)
- [IConvertSolidFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~BendRadius.html)

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
