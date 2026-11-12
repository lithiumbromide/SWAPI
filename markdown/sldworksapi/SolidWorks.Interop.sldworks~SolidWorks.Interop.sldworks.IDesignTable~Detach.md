---
title: "Detach Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "Detach"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.html"
---

# Detach Method (IDesignTable)

Detaches the design table from the Microsoft Excel sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Detach()
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable

instance.Detach()
```

### C#

```csharp
void Detach()
```

### C++/CLI

```cpp
void Detach();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DesignTable::Detach](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~Detach.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)
[Save Design Table as Microsoft Excel File (VBA)](Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm)
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

## Remarks

Call this method after you have finished using the other [IDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html) methods.

This function does not specifically deactivate the design table.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::Attach Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.html)
