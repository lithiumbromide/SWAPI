---
title: "IGetFilletItemAtIndex Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IGetFilletItemAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.html"
---

# IGetFilletItemAtIndex Method (ISimpleFilletFeatureData2)

Gets the fillet item at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFilletItemAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim Index As System.Integer
Dim value As System.Object

value = instance.IGetFilletItemAtIndex(Index)
```

### C#

```csharp
System.object IGetFilletItemAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ IGetFilletItemAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of fillet item

### Return Value

Fillet item: [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html), or NULL if the operation fails

## VBA Syntax

See [SimpleFilletFeatureData2::IGetFilletItemAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~IGetFilletItemAtIndex.html).

## Remarks

Call [ISimpleFilletFeatureData2::FilletItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~FilletItemsCount.html) before calling this method to determine the value for Index.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html)
[ISimpleFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetConicRhoOrRadius.html)
[ISimpleFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
