---
title: "FileName Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "FileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.html"
---

# FileName Property (IDesignTable)

Gets or sets the Microsoft Excel file for this design table.

## Syntax

### Visual Basic (Declaration)

```vb
Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.String

instance.FileName = value

value = instance.FileName
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Full path and filename for the Microsoft Excel file

## VBA Syntax

See [DesignTable::FileName](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~FileName.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::SaveAsExcelFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.html)
[IDesignTable::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.html)
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
