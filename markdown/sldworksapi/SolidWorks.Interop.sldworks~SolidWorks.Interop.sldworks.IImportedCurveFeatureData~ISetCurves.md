---
title: "ISetCurves Method (IImportedCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IImportedCurveFeatureData"
member: "ISetCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~ISetCurves.html"
---

# ISetCurves Method (IImportedCurveFeatureData)

Sets the curves for this imported curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetCurves( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IImportedCurveFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object

instance.ISetCurves(Count, DispArr)
```

### C#

```csharp
void ISetCurves(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
void ISetCurves(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of curves
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of curves of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.html)
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.html)
[IImportedCurveFeatureData::GetCurveCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~GetCurveCount.html)
[IImportedCurveFeatureData::IGetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~IGetCurves.html)
[IImportedCurveFeatureData::Curves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~Curves.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
