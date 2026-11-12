---
title: "InsertSlicing Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSlicing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSlicing.html"
---

# InsertSlicing Method (IFeatureManager)

Creates and inserts slicing into the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSlicing( _
   ByVal SlicingData As System.Object, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim SlicingData As System.Object
Dim Errors As System.Integer
Dim value As System.Object

value = instance.InsertSlicing(SlicingData, Errors)
```

### C#

```csharp
System.object InsertSlicing(
   System.object SlicingData,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ InsertSlicing(
   System.Object^ SlicingData,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SlicingData`: [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) (see **Remarks**)
- `Errors`: Errors as defined in [swInsertSlicingError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertSlicingError_e.html)

### Return Value

Array of sketch and reference plane objects

## VBA Syntax

See [FeatureManager::InsertSlicing](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSlicing.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

This method invokes the Slicing tool. For more information, refer to **SOLIDWORKS Help > Parts and Features > Controlling Parts > Slicing Tool**.

Before calling this method:

1. Pre-select in the graphics area a planar entity (to create a linear pattern of slices) or a combination of a linear entity and a point entity (to create an angular pattern of slices whose axis is the linear entity).
2. Use [IFeatureManager::GetSlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetSlicingData.html) to get an ISlicingData object.
3. Set [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.html) if step 1 is not performed. Specify a planar entity or a combination of a linear entity and a point entity as specified in step 1.
4. Set other ISlicingData properties.
5. Populate SlicingData with the ISlicingData object.

After calling this method:

- Use the array of sketch and reference plane objects returned by this method to perform further work.
- If [ISlicingData::AddSlicingPlanesAndSketchesToFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~AddSlicingPlanesAndSketchesToFolder.html) was set to true, then a **Slice1** folder in the FeatureManager design tree is created containing the slicing planes and sketches. You can edit the slicing planes and sketches individually as needed.
- Delete the Slice1 folder and its contents to remove slicing from the model.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
