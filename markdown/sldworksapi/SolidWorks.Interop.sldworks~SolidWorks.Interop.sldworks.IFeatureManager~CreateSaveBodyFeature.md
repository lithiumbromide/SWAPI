---
title: "CreateSaveBodyFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateSaveBodyFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateSaveBodyFeature.html"
---

# CreateSaveBodyFeature Method (IFeatureManager)

Creates a Save Bodies feature and creates part and assembly documents of the save bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSaveBodyFeature( _
   ByVal Bodies As System.Object, _
   ByVal FilePaths As System.Object, _
   ByVal AssemName As System.String, _
   ByVal ConsumeBody As System.Boolean, _
   ByVal CopyCustomProperty As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Bodies As System.Object
Dim FilePaths As System.Object
Dim AssemName As System.String
Dim ConsumeBody As System.Boolean
Dim CopyCustomProperty As System.Boolean
Dim value As System.Object

value = instance.CreateSaveBodyFeature(Bodies, FilePaths, AssemName, ConsumeBody, CopyCustomProperty)
```

### C#

```csharp
System.object CreateSaveBodyFeature(
   System.object Bodies,
   System.object FilePaths,
   System.string AssemName,
   System.bool ConsumeBody,
   System.bool CopyCustomProperty
)
```

### C++/CLI

```cpp
System.Object^ CreateSaveBodyFeature(
   System.Object^ Bodies,
   System.Object^ FilePaths,
   System.String^ AssemName,
   System.bool ConsumeBody,
   System.bool CopyCustomProperty
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bodies`: - Array of [solid bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) to save as parts (See **Remarks)**
- `FilePaths`: - Array of paths and filenames of the part documents to which to save Bodies
- `AssemName`: Path and filename of the assembly document to which to save Bodies
- `ConsumeBody`: See **Remarks**
- `CopyCustomProperty`: See **Remarks**

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::CreateSaveBodyFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateSaveBodyFeature.html).

## Examples

[Create Save Bodies Feature and Create an Assembly (VBA)](Create_Save_Bodies_Feature_and_Create_Assembly_Example_VB.htm)

## Remarks

If any solid bodies in Bodies are invalid, they are skipped/ignored.

| For parameter... | Specify... |
| --- | --- |
| ConsumeBody | VARIANT_TRUE (-1) to consume all bodies in the original part, VARIANT_FALSE (0) to not |
| CopyCustomProperty | VARIANT_TRUE (-1) to copy custom properties to the new parts, VARIANT_FALSE (0) to not |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
