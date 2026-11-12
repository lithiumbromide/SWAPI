---
title: "EditTable2 Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "EditTable2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.html"
---

# EditTable2 Method (IDesignTable)

Lets you edit the design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditTable2( _
   ByVal NewWindow As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim NewWindow As System.Boolean
Dim value As System.Object

value = instance.EditTable2(NewWindow)
```

### C#

```csharp
System.object EditTable2(
   System.bool NewWindow
)
```

### C++/CLI

```cpp
System.Object^ EditTable2(
   System.bool NewWindow
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewWindow`: True to edit the design table in a separate window, false to not

### Return Value

Microsoft Excel worksheet for this design table

## VBA Syntax

See [DesignTable::EditTable2](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~EditTable2.html).

## Examples

[Disable Cell Drop-down Lists in Design Table (C#)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm)
[Disable Cell Drop-down Lists in Design Table (VB.NET)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm)
[Disable Cell Drop-down Lists in Design Table (VBA)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm)

## Remarks

Do not use this method and [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html) in the same macro. Using IDesignTable::EditTable2 is preferable because it returns a pointer to the Microsoft Excel worksheet being operated on.

To avoid problems with zooming, set bNewWindow to True.

You can change the parameter values in the cells, add rows for additional configurations, or add columns to control additional parameters.

If the return value of this method is assigned to a variable, then it must be released before closing the design table with [IDesignTable::UpdateTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~UpdateTable.html)(type, True).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.html)
[IDesignTable::Updatable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Updatable.html)
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.html)
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4
