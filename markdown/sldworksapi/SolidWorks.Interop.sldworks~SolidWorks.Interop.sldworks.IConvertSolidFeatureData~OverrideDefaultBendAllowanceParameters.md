---
title: "OverrideDefaultBendAllowanceParameters Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "OverrideDefaultBendAllowanceParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultBendAllowanceParameters.html"
---

# OverrideDefaultBendAllowanceParameters Property (IConvertSolidFeatureData)

Sets whether to override the default custom bend allowance.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDefaultBendAllowanceParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.OverrideDefaultBendAllowanceParameters = value

value = instance.OverrideDefaultBendAllowanceParameters
```

### C#

```csharp
System.bool OverrideDefaultBendAllowanceParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDefaultBendAllowanceParameters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override, false to not

## VBA Syntax

See [ConvertSolidFeatureData::OverrideDefaultBendAllowanceParameters](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~OverrideDefaultBendAllowanceParameters.html).

## Remarks

Set this property to true when you want to override the bend allowance that is inherited by default from a parent sheet metal feature. Then [Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GetFixedFace.html) IConvertSolidFeatureData with new [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html) values for the subsequent sheet metal features.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
