---
title: "LoadPointsFromFile Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "LoadPointsFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~LoadPointsFromFile.html"
---

# LoadPointsFromFile Method (ITablePatternFeatureData)

Loads the location points of the table-driven pattern from a *.sldptab file.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadPointsFromFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim FileName As System.String
Dim value As System.Boolean

value = instance.LoadPointsFromFile(FileName)
```

### C#

```csharp
System.bool LoadPointsFromFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool LoadPointsFromFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the file with the table-driven pattern feature's point locations

### Return Value

True if the file loads successfully, false if not

## VBA Syntax

See [TablePatternFeatureData::LoadPointsFromFile](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~LoadPointsFromFile.html).

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::SavePointsToFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SavePointsToFile.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
