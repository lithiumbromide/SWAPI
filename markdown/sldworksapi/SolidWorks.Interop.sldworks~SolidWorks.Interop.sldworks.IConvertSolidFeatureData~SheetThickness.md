---
title: "SheetThickness Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "SheetThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~SheetThickness.html"
---

# SheetThickness Property (IConvertSolidFeatureData)

Gets or sets the sheet thickness of this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Double

instance.SheetThickness = value

value = instance.SheetThickness
```

### C#

```csharp
System.double SheetThickness {get; set;}
```

### C++/CLI

```cpp
property System.double SheetThickness {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Sheet thickness

## VBA Syntax

See

[ConvertSolidFeatureData::SheetThickness](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~SheetThickness.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## Remarks

The setter of this property is valid only if

[IConvertSolidFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultSheetMetalParameters.html)

is true.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
