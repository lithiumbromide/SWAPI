---
title: "IsMultipleRadius Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IsMultipleRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.html"
---

# IsMultipleRadius Property (ISimpleFilletFeatureData2)

Gets or sets whether this symmetric fillet or chamfer feature is a multiple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsMultipleRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.IsMultipleRadius = value

value = instance.IsMultipleRadius
```

### C#

```csharp
System.bool IsMultipleRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool IsMultipleRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this symmetric fillet/chamfer feature has multiple radii, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::IsMultipleRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~IsMultipleRadius.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

This property is valid only for symmetric constant radius fillets and symmetric offset face chamfers.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html)
[ISimpleFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html)
[ISimpleFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
