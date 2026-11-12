---
title: "ProcessByLevel Property (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "ProcessByLevel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.html"
---

# ProcessByLevel Property (IImportIgesData)

Gets or sets whether to process surfaces together.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProcessByLevel As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim value As System.Boolean

instance.ProcessByLevel = value

value = instance.ProcessByLevel
```

### C#

```csharp
System.bool ProcessByLevel {get; set;}
```

### C++/CLI

```cpp
property System.bool ProcessByLevel {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to process surfaces on the same IGES level together in their own folder in the FeatureManager design tree, false to process surfaces to level 0 and not put them in their own folder in the FeatureManager design tree

## VBA Syntax

See [ImportIgesData::ProcessByLevel](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~ProcessByLevel.html).

## Examples

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)
[IImportIgesData::SetLevels Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.html)
[IImportIgesData::IncludeAllLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels.html)
[IImportIgesData::IncludeOnlyLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.html)
[IImportIgesData::IncludeSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeSurfaces.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
