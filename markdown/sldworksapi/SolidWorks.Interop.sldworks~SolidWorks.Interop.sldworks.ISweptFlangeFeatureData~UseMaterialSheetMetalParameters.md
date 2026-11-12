---
title: "UseMaterialSheetMetalParameters Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "UseMaterialSheetMetalParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseMaterialSheetMetalParameters.html"
---

# UseMaterialSheetMetalParameters Property (ISweptFlangeFeatureData)

Gets or sets whether to use the material sheet metal parameters in this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseMaterialSheetMetalParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
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

See [SweptFlangeFeatureData::UseMaterialSheetMetalParameters](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~UseMaterialSheetMetalParameters.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

This property is valid only:

- when not creating the swept flange on an existing sheet metal feature,

- and -

- when [ISweptFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.html) is false.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
