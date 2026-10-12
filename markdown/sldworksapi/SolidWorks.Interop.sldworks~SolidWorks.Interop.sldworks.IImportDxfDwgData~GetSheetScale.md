---
title: "GetSheetScale Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetSheetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetSheetScale.html"
---

# GetSheetScale Method (IImportDxfDwgData)

Gets the sheet scale for the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSheetScale( _
   ByVal Sheet As System.String, _
   ByRef Numerator As System.Double, _
   ByRef Denominator As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Numerator As System.Double
Dim Denominator As System.Double

instance.GetSheetScale(Sheet, Numerator, Denominator)
```

### C#

```csharp
void GetSheetScale(
   System.string Sheet,
   out System.double Numerator,
   out System.double Denominator
)
```

### C++/CLI

```cpp
void GetSheetScale(
   System.String^ Sheet,
   [Out] System.double Numerator,
   [Out] System.double Denominator
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Numerator`: Numerator of the scale
- `Denominator`: Denominator of the scale

## VBA Syntax

See [ImportDxfDwgData::GetSheetScale](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetSheetScale.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::SetSheetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetSheetScale.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
