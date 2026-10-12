---
title: "InsertDeleteFace2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertDeleteFace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDeleteFace2.html"
---

# InsertDeleteFace2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::InsertDeleteFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertDeleteFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDeleteFace2( _
   ByVal Refill As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Refill As System.Integer
Dim value As System.Boolean

value = instance.InsertDeleteFace2(Refill)
```

### C#

```csharp
System.bool InsertDeleteFace2(
   System.int Refill
)
```

### C++/CLI

```cpp
System.bool InsertDeleteFace2(
   System.int Refill
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Refill`: - 1 refills the face after it is deleted
  - 0 does not

### Return Value

True if a [DeleteFace feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteFaceFeatureData.html) is inserted in the model, false if not

## VBA Syntax

See [ModelDoc2::InsertDeleteFace2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertDeleteFace2.html).

## Examples

[Delete Selected Faces (VBA)](Delete_Selected_Faces_Example_VB.htm)

## Remarks

This is a part-level operation and only works when the model is a [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IFeatureManager::EditDeleteFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditDeleteFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
