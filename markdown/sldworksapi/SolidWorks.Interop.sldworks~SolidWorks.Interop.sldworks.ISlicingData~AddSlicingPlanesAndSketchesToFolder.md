---
title: "AddSlicingPlanesAndSketchesToFolder Property (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "AddSlicingPlanesAndSketchesToFolder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~AddSlicingPlanesAndSketchesToFolder.html"
---

# AddSlicingPlanesAndSketchesToFolder Property (ISlicingData)

Gets or sets whether to add slicing planes and sketches to a folder in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property AddSlicingPlanesAndSketchesToFolder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Boolean

instance.AddSlicingPlanesAndSketchesToFolder = value

value = instance.AddSlicingPlanesAndSketchesToFolder
```

### C#

```csharp
System.bool AddSlicingPlanesAndSketchesToFolder {get; set;}
```

### C++/CLI

```cpp
property System.bool AddSlicingPlanesAndSketchesToFolder {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to add slicing planes and sketches to a folder in the FeatureManager design tree, false to not

## VBA Syntax

See [SlicingData::AddSlicingPlanesAndSketchesToFolder](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~AddSlicingPlanesAndSketchesToFolder.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

If this property is set to true, then after slicing, a **Slice1** folder is created in the FeatureManager design tree from which you can explicitly select and edit the slicing sketches and reference planes.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
