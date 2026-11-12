---
title: "Bends Property (IFoldsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFoldsFeatureData"
member: "Bends"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~Bends.html"
---

# Bends Property (IFoldsFeatureData)

Gets or sets the bend features for this fold feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bends As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFoldsFeatureData
Dim value As System.Object

instance.Bends = value

value = instance.Bends
```

### C#

```csharp
System.object Bends {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Bends {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of bend [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FoldsFeatureData::Bends](ms-its:sldworksapivb6.chm::/sldworks~FoldsFeatureData~Bends.html).

## Examples

[Insert and Access Fold Feature (C#)](Insert_and_Access_Fold_Feature_Example_CSharp.htm)
[Insert and Access Fold Feature (VB.NET)](Insert_and_Access_Fold_Feature_Example_VBNET.htm)
[Insert and Access Fold Feature (VBA)](Insert_and_Access_Fold_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.html)
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.html)
[IFoldsFeatureData::IGetBends Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBends.html)
[IFoldsFeatureData::IGetBendsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBendsCount.html)
[IFoldsFeatureData::ISetBends Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~ISetBends.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
