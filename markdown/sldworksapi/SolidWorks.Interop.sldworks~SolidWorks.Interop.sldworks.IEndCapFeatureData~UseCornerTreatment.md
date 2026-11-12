---
title: "UseCornerTreatment Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "UseCornerTreatment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseCornerTreatment.html"
---

# UseCornerTreatment Property (IEndCapFeatureData)

Gets or sets whether to apply a corner treatment to this end cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseCornerTreatment As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Boolean

instance.UseCornerTreatment = value

value = instance.UseCornerTreatment
```

### C#

```csharp
System.bool UseCornerTreatment {get; set;}
```

### C++/CLI

```cpp
property System.bool UseCornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply a corner treatment, false to not

## VBA Syntax

See [EndCapFeatureData::UseCornerTreatment](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~UseCornerTreatment.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
