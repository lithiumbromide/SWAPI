---
title: "IncludeOnlyLevels Property (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "IncludeOnlyLevels"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.html"
---

# IncludeOnlyLevels Property (IImportIgesData)

Gets the levels (layers) to import.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IncludeOnlyLevels As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim value As System.Object

value = instance.IncludeOnlyLevels
```

### C#

```csharp
System.object IncludeOnlyLevels {get;}
```

### C++/CLI

```cpp
property System.Object^ IncludeOnlyLevels {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) indicating the levels to import

## VBA Syntax

See [ImportIgesData::IncludeOnlyLevels](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~IncludeOnlyLevels.html).

## Remarks

[IImportIgesData::IncludeAllLevels](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~IncludeAllLevels.html) must be false to use this property.

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.html)
[IImportIgesData::SetLevels Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
