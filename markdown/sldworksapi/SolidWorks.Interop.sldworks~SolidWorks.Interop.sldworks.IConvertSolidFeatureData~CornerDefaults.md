---
title: "CornerDefaults Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "CornerDefaults"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~CornerDefaults.html"
---

# CornerDefaults Property (IConvertSolidFeatureData)

Gets or sets the sheet metal corner type in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerDefaults As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Integer

instance.CornerDefaults = value

value = instance.CornerDefaults
```

### C#

```csharp
System.int CornerDefaults {get; set;}
```

### C++/CLI

```cpp
property System.int CornerDefaults {
   System.int get();
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Sheet metal corner type as defined by

[swSheetMetalOverlapTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalOverlapTypes_e.html)

## VBA Syntax

See

[ConvertSolidFeatureData::CornerDefaults](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~CornerDefaults.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
