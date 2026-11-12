---
title: "SourceType Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "SourceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.html"
---

# SourceType Property (IDesignTable)

Gets or sets the type of source file for this design table.

## Syntax

### Visual Basic (Declaration)

```vb
Property SourceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

instance.SourceType = value

value = instance.SourceType
```

### C#

```csharp
System.int SourceType {get; set;}
```

### C++/CLI

```cpp
property System.int SourceType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of source file as defined in [swDesignTableSourceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDesignTableSourceTypes_e.html)

## VBA Syntax

See [DesignTable::SourceType](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~SourceType.html).

## Remarks

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html) after setting this property.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.html)
[IDesignTable::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.html)
[IDesignTable::SaveAsExcelFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
