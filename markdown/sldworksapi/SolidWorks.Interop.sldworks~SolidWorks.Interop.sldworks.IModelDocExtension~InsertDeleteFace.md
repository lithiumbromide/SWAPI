---
title: "InsertDeleteFace Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertDeleteFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDeleteFace.html"
---

# InsertDeleteFace Method (IModelDocExtension)

Inserts a DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDeleteFace( _
   ByVal Option As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Option As System.Integer
Dim value As System.Boolean

value = instance.InsertDeleteFace(Option)
```

### C#

```csharp
System.bool InsertDeleteFace(
   System.int Option
)
```

### C++/CLI

```cpp
System.bool InsertDeleteFace(
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: Option as defined in [swFaceDeleteOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceDeleteOption_e.html)

### Return Value

True if a DeleteFace feature is inserted, false if not

## VBA Syntax

See [ModelDocExtension::InsertDeleteFace](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertDeleteFace.html).

## Examples

[Insert and Change DeleteFace Feature (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)
[Insert and Change DeleteFace Feature (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

## Remarks

This is a part-level operation and only works when the model is a [part document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IFeatureManager::EditDeleteFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditDeleteFace.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
