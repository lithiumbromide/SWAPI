---
title: "ISlicingData Interface"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html"
---

# ISlicingData Interface

Allows access to slicing tool data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISlicingData
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
```

### C#

```csharp
public interface ISlicingData
```

### C++/CLI

```cpp
public interface class ISlicingData
```

## VBA Syntax

See [SlicingData](ms-its:sldworksapivb6.chm::/sldworks~SlicingData.html).

## Examples

'VBA

'Preconditions:

' 1. Open `Public_Documents`**\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\cube.sldprt**.

' 2. Change units to MKS.

' 3. Open the Immediate window.

'Postconditions:

' 1. Selects **Front Plane** as the first slicing plane.

' 2. Gets the default slicing parameters.

' 3. Specifies new slicing parameters.

' 4. Performs slicing and adds **Slice1** to the FeatureManager design tree.

' 5. Inspect the graphics area and the Immediate window.

' NOTE: Because the model is used elsewhere, do not save changes to it.

'===================================================
Dim swApp As SldWorks.SldWorks
Dim modDoc As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager
Dim sliceData As SldWorks.SlicingData
Dim boolstatus As Boolean
Dim errors As Long
Dim vars As Variant

Option Explicit

Sub main()

Set swApp = Application.SldWorks
Set modDoc = swApp.ActiveDoc
Set swFeatMgr = modDoc.FeatureManager

' Select the first slicing plane
boolstatus = modDoc.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
' Get default slicing parameters
Set sliceData = swFeatMgr.**GetSlicingData**()

Debug.Print "Default slicing values:"
Debug.Print ""
Debug.Print "Bounding box direction 1: " & sliceData.**GetBoundingBoxDirection1**
Debug.Print "Bounding box direction 2: " & sliceData.**GetBoundingBoxDirection2**
Debug.Print "Bounding box direction 3: " & sliceData.**GetBoundingBoxDirection3**
Debug.Print "Bounding box direction 4: " & sliceData.**GetBoundingBoxDirection4**
Debug.Print "Reverse direction? " & sliceData.**ReverseDirection**
Debug.Print "Number of slices: " & sliceData.**NumberOfPlanes**
Debug.Print "Distance between slices: " & sliceData.**Offset**
Debug.Print "Type of slicing as defined in swSlicingTypes_e: " & sliceData.**SlicesToGenerate**
Debug.Print "Add slicing planes and sketches to folder? " & sliceData.**AddSlicingPlanesAndSketchesToFolder**

sliceData.**ReverseDirection** = False
boolstatus = sliceData.**SetBoundingBoxDirection1**(0.1397)
boolstatus = sliceData.**SetBoundingBoxDirection2**(0.1397)
boolstatus = sliceData.**SetBoundingBoxDirection3**(-0.1397)
boolstatus = sliceData.**SetBoundingBoxDirection4**(-0.1397)
sliceData.**NumberOfPlanes** = 6
sliceData.**Offset** = 0.01
sliceData.**SlicesToGenerate** = swSlicingTypes_Rectangle
sliceData.**AddSlicingPlanesAndSketchesToFolder** = True

Debug.Print ""
Debug.Print "New values:"
Debug.Print ""
Debug.Print "Bounding box direction 1: " & sliceData.**GetBoundingBoxDirection1**
Debug.Print "Bounding box direction 2: " & sliceData.**GetBoundingBoxDirection2**
Debug.Print "Bounding box direction 3: " & sliceData.**GetBoundingBoxDirection3**
Debug.Print "Bounding box direction 4: " & sliceData.**GetBoundingBoxDirection4**
Debug.Print "Reverse direction? " & sliceData.**ReverseDirection**
Debug.Print "Number of slices: " & sliceData.**NumberOfPlanes**
Debug.Print "Distance between slices: " & sliceData.**Offset**
Debug.Print "Type of slicing as defined in swSlicingTypes_e: " & sliceData.**SlicesToGenerate**
Debug.Print "Add slicing planes and sketches to folder? " & sliceData.**AddSlicingPlanesAndSketchesToFolder**

vars = swFeatMgr.**InsertSlicing**(sliceData, errors)

Debug.Print ""
Debug.Print "Slicing error code as defined in swInsertSlicingError_e: " & errors

End Sub

## Examples

[Slice a Model (C#)](Slice_a_Model_Example_CSharp.htm)

## Remarks

You must pre-select the first slicing plane before you can access the default bounding box directions for slicing.

[IFeatureManager::InsertSlicing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSlicing.html) takes this data object and invokes the Slicing tool. The Slicing tool creates a parallel or radial series of slicing planes with sketches that intersect, or slice, the model.

For more information, see the **Slicing Tool** topics in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeatureManager::GetSlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetSlicingData.html)

## Access Diagram

[SlicingData](SWObjectModel.pdf#SlicingData)

## See Also

[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
