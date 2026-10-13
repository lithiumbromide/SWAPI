---
title: "GetFeatureCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureCount.html"
---

# GetFeatureCount Method (IModelDoc2)

Gets the number of features in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetFeatureCount()
```

### C#

```csharp
System.int GetFeatureCount()
```

### C++/CLI

```cpp
System.int GetFeatureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of features in this document; this number does not include subfeatures

## VBA Syntax

See [ModelDoc2::GetFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetFeatureCount.html).

## Examples

[Traverse Features By Reverse Position (C#)](Traverse_Features_By_Reverse_Position_Example_CSharp.htm)
[Traverse Features By Reverse Position (VB.NET)](Traverse_Features_By_Reverse_Position_Example_VBNET.htm)
[Traverse Features By Reverse Position (VBA)](Traverse_Features_By_Reverse_Position_Example_VB.htm)
[Get Features in Reverse Order (C#)](Get_Features_in_Reverse_Order_Example_CSharp.htm)
[Get Features in Reverse Order (VB.NET)](Get_Features_in_Reverse_Order_Example_VBNET.htm)
[Get Features in Reverse Order (VBA)](Get_Features_in_Reverse_Order_Example_VB.htm)

## Remarks

The number of features returned by this method does not include subfeatures. Subfeatures include, for example, mate features within a mategroup, drawing views on a sheet, and so on. One way to identify a subfeature is whether it can be returned by:

- [IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html) or [IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html)
- [IFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextSubFeature.html) or [IFeature::IGetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextSubFeature.html).

This method returns the number of features returned when traversing the Feature list with [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html) or [IModelDoc2::IFirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFirstFeature.html) and [IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html) or [IFeature::IGetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextFeature.html). This value may be useful in feature traversal or if accessing the feature by position using [IModelDoc2::FeatureByPositionReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.html) or [IModelDoc2::IFeatureByPositionReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
