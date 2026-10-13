---
title: "GetPosition Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPosition.html"
---

# GetPosition Method (IImportDxfDwgData)

Gets the position of the entities created in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetPosition( _
   ByVal Sheet As System.String, _
   ByRef Positioning As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Positioning As System.Integer
Dim X As System.Double
Dim Y As System.Double

instance.GetPosition(Sheet, Positioning, X, Y)
```

### C#

```csharp
void GetPosition(
   System.string Sheet,
   out System.int Positioning,
   out System.double X,
   out System.double Y
)
```

### C++/CLI

```cpp
void GetPosition(
   System.String^ Sheet,
   [Out] System.int Positioning,
   [Out] System.double X,
   [Out] System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Positioning`: Position as defined in [swDwgImportEntitiesPositioning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgImportEntitiesPositioning_e.html)
- `X`: X coordinate of the origin of the imported drawing
- `Y`: Y coordinate of the origin of the imported drawing

## VBA Syntax

See [ImportDxfDwgData::GetPosition](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetPosition.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPosition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
