---
title: "GetItems Method (ILayer)"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: "GetItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetItems.html"
---

# GetItems Method (ILayer)

Gets the items on this layer.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetItems( _
   ByVal ItemType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
Dim ItemType As System.Integer
Dim value As System.Object

value = instance.GetItems(ItemType)
```

### C#

```csharp
System.object GetItems(
   System.int ItemType
)
```

### C++/CLI

```cpp
System.Object^ GetItems(
   System.int ItemType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ItemType`: Items to get as defined in [swLayerItemsOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLayerItemsOption_e.html)

### Return Value

Array of layer items

## VBA Syntax

See [Layer::GetItems](ms-its:sldworksapivb6.chm::/sldworks~Layer~GetItems.html).

## See Also

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
