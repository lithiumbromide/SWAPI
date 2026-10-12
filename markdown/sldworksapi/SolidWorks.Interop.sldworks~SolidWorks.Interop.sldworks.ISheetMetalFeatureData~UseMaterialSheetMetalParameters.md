---
title: "UseMaterialSheetMetalParameters Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "UseMaterialSheetMetalParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseMaterialSheetMetalParameters.html"
---

# UseMaterialSheetMetalParameters Property (ISheetMetalFeatureData)

Gets or sets whether to use the properties of the material applied when creating this sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseMaterialSheetMetalParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Boolean

instance.UseMaterialSheetMetalParameters = value

value = instance.UseMaterialSheetMetalParameters
```

### C#

```csharp
System.bool UseMaterialSheetMetalParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool UseMaterialSheetMetalParameters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the material sheet metal parameters, false to not

## VBA Syntax

See [SheetMetalFeatureData::UseMaterialSheetMetalParameters](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~UseMaterialSheetMetalParameters.html).

## Remarks

This property is valid only when [ISheetMetalFeatureData::GetUseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.html) returns false.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
