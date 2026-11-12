---
title: "IsActive Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "IsActive"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.html"
---

# IsActive Method (IDesignTable)

Gets whether the design table is currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsActive() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

value = instance.IsActive()
```

### C#

```csharp
System.bool IsActive()
```

### C++/CLI

```cpp
System.bool IsActive();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True If design table is currently being edited, false if not

## VBA Syntax

See [DesignTable::IsActive](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~IsActive.html).

## Examples

[Save Design Table as Microsoft Excel File (VBA)](Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::EditFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html)
[IDesignTable::EditTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.html)
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html)
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.html)
[IDesignTable::UpdateTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.html)
[IDesignTable::Updatable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Updatable.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
