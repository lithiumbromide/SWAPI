---
title: "FilletItemsCount Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "FilletItemsCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~FilletItemsCount.html"
---

# FilletItemsCount Property (ISimpleFilletFeatureData2)

Gets the number of fillets for this simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FilletItemsCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

value = instance.FilletItemsCount
```

### C#

```csharp
System.int FilletItemsCount {get;}
```

### C++/CLI

```cpp
property System.int FilletItemsCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of fillets

## VBA Syntax

See [SimpleFilletFeatureData2::FilletItemsCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~FilletItemsCount.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

This method returns -1 if this simple fillet feature is not multiple radius.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFilletItemAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html)
[ISimpleFilletFeatureData2::IGetFilletItemAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.html)
[ISimpleFilletFeatureData2::GetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html)
[ISimpleFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
