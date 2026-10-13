---
title: "Worksheet Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "Worksheet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Worksheet.html"
---

# Worksheet Property (IDesignTable)

Gets the Microsoft Excel worksheet for this design table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Worksheet As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Object

value = instance.Worksheet
```

### C#

```csharp
System.object Worksheet {get;}
```

### C++/CLI

```cpp
property System.Object^ Worksheet {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Microsoft Excel worksheet for this design table

## VBA Syntax

See [DesignTable::Worksheet](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~Worksheet.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

## Remarks

Before you can call this method, you must call [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.html)
[IDesignTable::SaveAsExcelFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.html)
[IDesignTable::Detach Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.html)
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
