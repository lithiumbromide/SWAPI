---
title: "Options Property (IDeleteFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteFaceFeatureData"
member: "Options"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~Options.html"
---

# Options Property (IDeleteFaceFeatureData)

Gets or sets the option for the DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteFaceFeatureData
Dim value As System.Integer

instance.Options = value

value = instance.Options
```

### C#

```csharp
System.int Options {get; set;}
```

### C++/CLI

```cpp
property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Option as defined in [swFaceDeleteOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceDeleteOption_e.html)

## VBA Syntax

See [DeleteFaceFeatureData::Options](ms-its:sldworksapivb6.chm::/sldworks~DeleteFaceFeatureData~Options.html).

## Examples

[Insert and Change DeleteFace Feature (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)
[Insert and Change DeleteFace Feature (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
