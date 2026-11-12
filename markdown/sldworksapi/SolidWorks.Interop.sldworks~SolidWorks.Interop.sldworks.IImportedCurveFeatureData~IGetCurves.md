---
title: "IGetCurves Method (IImportedCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IImportedCurveFeatureData"
member: "IGetCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~IGetCurves.html"
---

# IGetCurves Method (IImportedCurveFeatureData)

Gets the curves for this imported curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurves( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IImportedCurveFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetCurves(Count)
```

### C#

```csharp
System.object IGetCurves(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetCurves(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of curves

### Return Value

- in-process, unmanaged C++: Pointer to an array of curves of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IImportedCurveFeatureData::GetCurveCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportedCurveFeatureData~GetCurveCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.html)
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.html)
[IImportedCurveFeatureData::ISetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~ISetCurves.html)
[IImportedCurveFeatureData::Curves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~Curves.html)

## Availability

SOLIDWORKS 2003 FCS, Revision number 11.0
