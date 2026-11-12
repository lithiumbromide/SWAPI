---
title: "IncludeCurves Property (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "IncludeCurves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeCurves.html"
---

# IncludeCurves Property (IImportIgesData)

Gets or sets whether or not to import curves.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeCurves As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim value As System.Boolean

instance.IncludeCurves = value

value = instance.IncludeCurves
```

### C#

```csharp
System.bool IncludeCurves {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeCurves {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import curves, false to not

## VBA Syntax

See [ImportIgesData::IncludeCurves](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~IncludeCurves.html).

## Examples

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## Remarks

If this property is True, then you can use [IImportIgesData::CurvesAsSketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~CurvesAsSketches.html) to specify whether to import curves as sketches or as reference curve features.

Use [IImportIgesData::IncludeSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~IncludeSurfaces.html) to indicate whether or not to import surfaces.

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
