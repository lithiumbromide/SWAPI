---
title: "Updatable Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "Updatable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Updatable.html"
---

# Updatable Property (IDesignTable)

Gets or sets whether edits to the model update the design table.

## Syntax

### Visual Basic (Declaration)

```vb
Property Updatable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

instance.Updatable = value

value = instance.Updatable
```

### C#

```csharp
System.bool Updatable {get; set;}
```

### C++/CLI

```cpp
property System.bool Updatable {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if edits to the model update the design table, false if not

## VBA Syntax

See [DesignTable::Updatable](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~Updatable.html).

## Examples

[Get or Set Whether Edits Update Design Table (VBA)](Get_or_Set_Whether_Edits_Update_Design_Table_Example_VB.htm)

## Remarks

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html) after setting this property.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::EditFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html)
[IDesignTable::EditTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.html)
[IDesignTable::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.html)
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html)
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.html)
[IDesignTable::UpdateTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
