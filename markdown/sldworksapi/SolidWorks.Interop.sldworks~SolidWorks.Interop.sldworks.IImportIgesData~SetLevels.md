---
title: "SetLevels Method (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "SetLevels"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.html"
---

# SetLevels Method (IImportIgesData)

Sets the levels-related information for importing and IGES file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLevels( _
   ByVal All As System.Boolean, _
   ByVal Only As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim All As System.Boolean
Dim Only As System.Object
Dim value As System.Boolean

value = instance.SetLevels(All, Only)
```

### C#

```csharp
System.bool SetLevels(
   System.bool All,
   System.object Only
)
```

### C++/CLI

```cpp
System.bool SetLevels(
   System.bool All,
   System.Object^ Only
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `All`: True to process all IGES levels, false to not
- `Only`: If All is false, then specify either a long or integer, or an array of longs or integers, indicating the levels to process

### Return Value

True if the levels-related information is set, false if not

## VBA Syntax

See [ImportIgesData::SetLevels](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~SetLevels.html).

## Examples

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)
[IImportIgesData::IncludeAllLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels.html)
[IImportIgesData::IncludeOnlyLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.html)
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
