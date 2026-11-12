---
title: "GetEdgeCount Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetEdgeCount.html"
---

# GetEdgeCount Method (ISimpleFilletFeatureData2)

Gets the number of edges on which to create a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

value = instance.GetEdgeCount()
```

### C#

```csharp
System.int GetEdgeCount()
```

### C++/CLI

```cpp
System.int GetEdgeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [SimpleFilletFeatureData2::GetEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetEdgeCount.html).

## Examples

[Get Simple Fillet Feature Data (VBA)](Get_Simple_Fillet_Feature_Data_Example_VB.htm)
[Get Simple Fillet Feature Data (VB.NET)](Get_Simple_Fillet_Feature_Data_Example_VBNET.htm)
[Get Simple Fillet Feature Data (C#)](Get_Simple_Fillet_Feature_Data_Example_CSharp.htm)

## Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetEdges.html) to get the size of the array for that method.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetEdges.html)
[ISimpleFilletFeatureData2::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Edges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
