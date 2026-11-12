---
title: "CurvesAsSketches Property (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "CurvesAsSketches"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~CurvesAsSketches.html"
---

# CurvesAsSketches Property (IImportIgesData)

Gets or sets whether the curves are imported as sketches or reference curve features.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurvesAsSketches As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim value As System.Boolean

instance.CurvesAsSketches = value

value = instance.CurvesAsSketches
```

### C#

```csharp
System.bool CurvesAsSketches {get; set;}
```

### C++/CLI

```cpp
property System.bool CurvesAsSketches {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import curves as sketches, false to import curves as reference curve features

## VBA Syntax

See [ImportIgesData::CurvesAsSketches](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~CurvesAsSketches.html).

## Examples

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## Remarks

[IImportIgesData::IncludeCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~IncludeCurves.html) must be set to true for this property to have an effect.

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
