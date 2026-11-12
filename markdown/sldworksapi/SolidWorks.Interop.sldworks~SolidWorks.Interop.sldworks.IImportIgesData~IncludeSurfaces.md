---
title: "IncludeSurfaces Property (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "IncludeSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeSurfaces.html"
---

# IncludeSurfaces Property (IImportIgesData)

Gets or sets whether to import surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSurfaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim value As System.Boolean

instance.IncludeSurfaces = value

value = instance.IncludeSurfaces
```

### C#

```csharp
System.bool IncludeSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeSurfaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import surfaces, false to not

## VBA Syntax

See [ImportIgesData::IncludeSurfaces](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~IncludeSurfaces.html).

## Examples

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## Remarks

To import curves, use [IImportIgesData::IncludeCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~IncludeCurves.html) and [IImportIgesData::CurvesAsSketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~CurvesAsSketches.html).

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
