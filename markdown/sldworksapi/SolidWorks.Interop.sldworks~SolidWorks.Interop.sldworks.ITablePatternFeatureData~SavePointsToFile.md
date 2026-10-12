---
title: "SavePointsToFile Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "SavePointsToFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SavePointsToFile.html"
---

# SavePointsToFile Method (ITablePatternFeatureData)

Saves the location of the table-driven pattern feature's points to a *.sldptab file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SavePointsToFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SavePointsToFile(FileName)
```

### C#

```csharp
System.bool SavePointsToFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SavePointsToFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the file to which to save the points

### Return Value

True if successful, false if not

## VBA Syntax

See [TablePatternFeatureData::SavePointsToFile](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~SavePointsToFile.html).

## Remarks

Exported units, e.g. meters, of the document that owns the feature, and not necessarily those of the active document, are used when data is saved to a file.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::LoadPointsFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~LoadPointsFromFile.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
