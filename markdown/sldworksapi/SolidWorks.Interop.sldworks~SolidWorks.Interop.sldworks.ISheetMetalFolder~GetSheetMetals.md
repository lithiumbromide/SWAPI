---
title: "GetSheetMetals Method (ISheetMetalFolder)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFolder"
member: "GetSheetMetals"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder~GetSheetMetals.html"
---

# GetSheetMetals Method (ISheetMetalFolder)

Gets the sheet metal features in this folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetMetals() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFolder
Dim value As System.Object

value = instance.GetSheetMetals()
```

### C#

```csharp
System.object GetSheetMetals()
```

### C++/CLI

```cpp
System.Object^ GetSheetMetals();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)s

## VBA Syntax

See [SheetMetalFolder::GetSheetMetals](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFolder~GetSheetMetals.html).

## Examples

See [ISheetMetalFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFolder.html) examples.

## See Also

[ISheetMetalFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder.html)
[ISheetMetalFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder_members.html)
[ISheetMetalFolder::GetSheetMetalCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder~GetSheetMetalCount.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
