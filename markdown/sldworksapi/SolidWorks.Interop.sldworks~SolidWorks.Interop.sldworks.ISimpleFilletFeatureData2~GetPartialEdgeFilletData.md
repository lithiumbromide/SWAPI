---
title: "GetPartialEdgeFilletData Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetPartialEdgeFilletData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetPartialEdgeFilletData.html"
---

# GetPartialEdgeFilletData Method (ISimpleFilletFeatureData2)

Gets the partial edge fillet data for the specified edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartialEdgeFilletData( _
   ByVal FilletItem As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim FilletItem As System.Object
Dim value As System.Object

value = instance.GetPartialEdgeFilletData(FilletItem)
```

### C#

```csharp
System.object GetPartialEdgeFilletData(
   System.object FilletItem
)
```

### C++/CLI

```cpp
System.Object^ GetPartialEdgeFilletData(
   System.Object^ FilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilletItem`: [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

### Return Value

[IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html); null if FilletItem is not an edge

## VBA Syntax

See [SimpleFilletFeatureData2::GetPartialEdgeFilletData](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetPartialEdgeFilletData.html).

## Examples

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html) example.

## Remarks

This method is valid only if [ISimpleFilletFeatureData2::EnablePartialEdgeParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.html) is true.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::SetPartialEdgeFilletData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetPartialEdgeFilletData.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
