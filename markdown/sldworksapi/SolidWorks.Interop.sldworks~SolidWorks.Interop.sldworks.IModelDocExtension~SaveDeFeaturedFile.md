---
title: "SaveDeFeaturedFile Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SaveDeFeaturedFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDeFeaturedFile.html"
---

# SaveDeFeaturedFile Method (IModelDocExtension)

Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer surface as a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveDeFeaturedFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SaveDeFeaturedFile(FileName)
```

### C#

```csharp
System.bool SaveDeFeaturedFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SaveDeFeaturedFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name for the new, de-featured part

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [ModelDocExtension::SaveDeFeaturedFile](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SaveDeFeaturedFile.html).

## Examples

[Save as De-Featured File (VBA)](Save_As_Defeatured_File_Example_VB.htm)
[Save as De-Featured File (VB.NET)](Save_As_Defeatured_File_Example_VBNET.htm)
[Save as De-Featured File (C#)](Save_As_Defeatured_File_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
