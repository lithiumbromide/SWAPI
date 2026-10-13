---
title: "FilletEdgeCount Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "FilletEdgeCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~FilletEdgeCount.html"
---

# FilletEdgeCount Property (IVariableFilletFeatureData2)

Gets the number of edges to fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FilletEdgeCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Integer

value = instance.FilletEdgeCount
```

### C#

```csharp
System.int FilletEdgeCount {get;}
```

### C++/CLI

```cpp
property System.int FilletEdgeCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of edges to fillet

## VBA Syntax

See [VariableFilletFeatureData2::FilletEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~FilletEdgeCount.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetFilletEdgeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.html)
[IVariableFilletFeatureData2::IGetFilletEdgeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
