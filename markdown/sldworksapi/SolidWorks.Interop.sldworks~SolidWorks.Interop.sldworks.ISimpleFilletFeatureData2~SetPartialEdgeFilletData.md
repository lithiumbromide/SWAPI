---
title: "SetPartialEdgeFilletData Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "SetPartialEdgeFilletData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetPartialEdgeFilletData.html"
---

# SetPartialEdgeFilletData Method (ISimpleFilletFeatureData2)

Sets the partial edge fillet data for the specified edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPartialEdgeFilletData( _
   ByVal FilletItem As System.Object, _
   ByVal PartialEdgeFilletData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim FilletItem As System.Object
Dim PartialEdgeFilletData As System.Object
Dim value As System.Boolean

value = instance.SetPartialEdgeFilletData(FilletItem, PartialEdgeFilletData)
```

### C#

```csharp
System.bool SetPartialEdgeFilletData(
   System.object FilletItem,
   System.object PartialEdgeFilletData
)
```

### C++/CLI

```cpp
System.bool SetPartialEdgeFilletData(
   System.Object^ FilletItem,
   System.Object^ PartialEdgeFilletData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilletItem`: [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
- `PartialEdgeFilletData`: [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html); null to remove existing partial edge fillet data from FilletItem

### Return Value

True if partial edge fillet data successfully set, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::SetPartialEdgeFilletData](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~SetPartialEdgeFilletData.html).

## Remarks

This method is valid only if [ISimpleFilletFeatureData2::EnablePartialEdgeParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.html) is true.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetPartialEdgeFilletData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetPartialEdgeFilletData.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
