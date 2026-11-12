---
title: "UseDefaultBendAllowance Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "UseDefaultBendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultBendAllowance.html"
---

# UseDefaultBendAllowance Property (ISweptFlangeFeatureData)

Gets or sets whether to use the bend allowance from the original sheet metal feature in this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendAllowance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.UseDefaultBendAllowance = value

value = instance.UseDefaultBendAllowance
```

### C#

```csharp
System.bool UseDefaultBendAllowance {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendAllowance {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the default bend allowance, false to use a custom bend allowance (see **Remarks**)

## VBA Syntax

See [SweptFlangeFeatureData::UseDefaultBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~UseDefaultBendAllowance.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

For cylindrical/conical swept flanges, this property is valid only during creation.

If this property is false, then use [ISweptFlangeFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetCustomBendAllowance.html) and [ISweptFlangeFeatureData::SetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetCustomBendAllowance.html) to get and set a custom bend allowance.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
