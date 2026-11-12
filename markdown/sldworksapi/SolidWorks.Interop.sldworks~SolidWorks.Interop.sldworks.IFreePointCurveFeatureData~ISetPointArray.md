---
title: "ISetPointArray Method (IFreePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFreePointCurveFeatureData"
member: "ISetPointArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~ISetPointArray.html"
---

# ISetPointArray Method (IFreePointCurveFeatureData)

Sets the list of X, Y, Z coordinates for the points for this free-point curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPointArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFreePointCurveFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Double

instance.ISetPointArray(FeatCount, ArrayDataIn)
```

### C#

```csharp
void ISetPointArray(
   System.int FeatCount,
   ref System.double ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetPointArray(
   System.int FeatCount,
   System.double% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatCount`: Number of features
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of doubles containing 3 * points (see **Remarks**)

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The ArrayDataIn argument is an array of doubles containing 3 * points:

[ x1, y1, z1, x2, y2, z2, ... ]

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.html)
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
