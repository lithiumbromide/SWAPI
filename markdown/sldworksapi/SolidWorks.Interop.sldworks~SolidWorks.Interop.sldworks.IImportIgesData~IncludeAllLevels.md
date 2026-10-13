---
title: "IncludeAllLevels Property (IImportIgesData)"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: "IncludeAllLevels"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels.html"
---

# IncludeAllLevels Property (IImportIgesData)

Gets whether all levels (layers) are imported.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IncludeAllLevels As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
Dim value As System.Boolean

value = instance.IncludeAllLevels
```

### C#

```csharp
System.bool IncludeAllLevels {get;}
```

### C++/CLI

```cpp
property System.bool IncludeAllLevels {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import all levels, false to not

## VBA Syntax

See [ImportIgesData::IncludeAllLevels](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData~IncludeAllLevels.html).

## Remarks

If this property is false, then you can use [IImportIgesData::IncludeOnlyLevels](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.html) to find out which levels will be processed.

## See Also

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.html)
[IImportIgesData::SetLevels Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
