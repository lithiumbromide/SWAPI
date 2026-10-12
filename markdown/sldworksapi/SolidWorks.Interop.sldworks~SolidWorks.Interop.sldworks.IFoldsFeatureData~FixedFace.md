---
title: "FixedFace Property (IFoldsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFoldsFeatureData"
member: "FixedFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~FixedFace.html"
---

# FixedFace Property (IFoldsFeatureData)

Gets or sets the fixed face of this fold feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFoldsFeatureData
Dim value As System.Object

instance.FixedFace = value

value = instance.FixedFace
```

### C#

```csharp
System.object FixedFace {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FixedFace {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fixed [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [FoldsFeatureData::FixedFace](ms-its:sldworksapivb6.chm::/sldworks~FoldsFeatureData~FixedFace.html).

## Examples

[Insert and Access Fold Feature (C#)](Insert_and_Access_Fold_Feature_Example_CSharp.htm)
[Insert and Access Fold Feature (VB.NET)](Insert_and_Access_Fold_Feature_Example_VBNET.htm)
[Insert and Access Fold Feature (VBA)](Insert_and_Access_Fold_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.html)
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
