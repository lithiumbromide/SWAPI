---
title: "UseDefaultBendAllowance Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "UseDefaultBendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendAllowance.html"
---

# UseDefaultBendAllowance Property (IBaseFlangeFeatureData)

Gets whether the bend allowance from the original sheet metal feature is used in this sheet metal base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UseDefaultBendAllowance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

value = instance.UseDefaultBendAllowance
```

### C#

```csharp
System.bool UseDefaultBendAllowance {get;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendAllowance {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the parent sheet metal bend allowance, false uses a custom bend allowance

## VBA Syntax

See [BaseFlangeFeatureData::UseDefaultBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~UseDefaultBendAllowancehtml).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

If this property is false, then use [IBaseFlangeFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetCustomBendAllowance.html) to get the custom bend allowance used to [initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html) this base flange.

Whether to use the default bend allowance is set during the initialization of this base flange and cannot be changed.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
