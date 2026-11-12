---
title: "UpdateTable Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "UpdateTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.html"
---

# UpdateTable Method (IDesignTable)

Applies the changes made to the design table to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateTable( _
   ByVal Type As System.Integer, _
   ByVal Close As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim Type As System.Integer
Dim Close As System.Boolean
Dim value As System.Boolean

value = instance.UpdateTable(Type, Close)
```

### C#

```csharp
System.bool UpdateTable(
   System.int Type,
   System.bool Close
)
```

### C++/CLI

```cpp
System.bool UpdateTable(
   System.int Type,
   System.bool Close
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of update as defined in [swDesignTableUpdateOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDesignTableUpdateOptions_e.html)
- `Close`: True to close the design table, false to not

### Return Value

True if the changes made to the design table update the model, false if not

## VBA Syntax

See [DesignTable::UpdateTable](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~UpdateTable.html).

## Examples

[Add Row to Design Table (VBA)](Add_Row_to_Design_Table_Example_VB.htm)
[Disable Cell Drop-down Lists in Design Table (C#)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm)
[Disable Cell Drop-down Lists in Design Table (VB.NET)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm)
[Disable Cell Drop-down Lists in Design Table (VBA)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm)

## Remarks

[IDesignTable::UpdateModel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~UpdateModel.html) is a simplified version of this method.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::EditFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html)
[IDesignTable::EditTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.html)
[IDesignTable::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.html)
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html)
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.html)
[IDesignTable::Warn Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Warn.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
