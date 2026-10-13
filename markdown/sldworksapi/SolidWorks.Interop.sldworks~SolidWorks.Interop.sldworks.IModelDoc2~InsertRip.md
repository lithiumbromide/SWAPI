---
title: "InsertRip Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRip.html"
---

# InsertRip Method (IModelDoc2)

Creates a rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRip( _
   ByVal Gap As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Gap As System.Double

instance.InsertRip(Gap)
```

### C#

```csharp
void InsertRip(
   System.double Gap
)
```

### C++/CLI

```cpp
void InsertRip(
   System.double Gap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Gap`: Size of the rip gap

## VBA Syntax

See [ModelDoc2::InsertRip](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRip.html).

## Examples

[Access Edges on Rip Feature (VBA)](Access_and_Release_Access_to_Edges_Example_VB.htm)
[Access Edges on Rip Feature (VB.NET)](Access_and_Release_Access_to_Edges_Example_VBNET.htm)
[Access Edges on Rip Feature (C#)](Access_and_Release_Access_to_Edges_Example_CSharp.htm)

## Remarks

The direction of the rip is determined by the Mark value used to select the edges along which to rip.

| Direction | Selection Mark | IRipFeatureData::GetDirection |
| --- | --- | --- |
| Current | 16 | 0 |
| Other | 32 | 1 |
| Both | 64 | 2 |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
