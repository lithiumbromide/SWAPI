---
title: "Attach Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "Attach"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.html"
---

# Attach Method (IDesignTable)

Activates the design table within the part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Attach() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

value = instance.Attach()
```

### C#

```csharp
System.bool Attach()
```

### C++/CLI

```cpp
System.bool Attach();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the design table is successfully activated, false if not

## VBA Syntax

See [DesignTable::Attach](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~Attach.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)
[Save Design Table as Microsoft Excel File (VBA)](Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)

## Remarks

If you want SOLIDWORKS to run in the background, then do not use this method. Using this method will cause SOLIDWORKS to become visible.

Do not use this method and [IDesignTable::EditTable2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~EditTable2.html) in the same macro. Using IDesignTable::EditTable2 is preferable because it returns a pointer to the Microsoft Excel worksheet being operated on.

If you use IDesignTable::Attach, then you must call this method before calling any of the other IDesignTable methods. When your application is finished extracting data from the design table, use [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html) to detach the IDesignTable object from the Microsoft Excel object.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
