---
title: "GetCurveCount Method (IImportedCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IImportedCurveFeatureData"
member: "GetCurveCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~GetCurveCount.html"
---

# GetCurveCount Method (IImportedCurveFeatureData)

Gets the number of curves for this imported curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurveCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IImportedCurveFeatureData
Dim value As System.Integer

value = instance.GetCurveCount()
```

### C#

```csharp
System.int GetCurveCount()
```

### C++/CLI

```cpp
System.int GetCurveCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of curves

## VBA Syntax

See [ImportedCurveFeatureData::GetCurveCount](ms-its:sldworksapivb6.chm::/sldworks~ImportedCurveFeatureData~GetCurveCount.html).

## Examples

[Get Imported Curve Feature Data (C#)](Get_Imported_Curve_Feature_Data_Example_CSharp.htm)
[Get Imported Curve Feature Data (VB.NET)](Get_Imported_Curve_Feature_Data_Example_VBNET.htm)
[Get Imported Curve Feature Data (VBA)](Get_Imported_Curve_Feature_Data_Example_VB.htm)

## Remarks

Call this method before calling [IImportedCurveFeatureData::IGetCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportedCurveFeatureData~IGetCurves.html).

## See Also

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.html)
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.html)
[IImportedCurveFeatureData::ISetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~ISetCurves.html)
[IImportedCurveFeatureData::Curves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~Curves.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
