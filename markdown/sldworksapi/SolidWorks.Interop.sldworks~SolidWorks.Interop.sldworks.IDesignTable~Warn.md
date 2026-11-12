---
title: "Warn Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "Warn"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Warn.html"
---

# Warn Property (IDesignTable)

Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table.

## Syntax

### Visual Basic (Declaration)

```vb
Property Warn As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

instance.Warn = value

value = instance.Warn
```

### C#

```csharp
System.bool Warn {get; set;}
```

### C++/CLI

```cpp
property System.bool Warn {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display a warning when invalid information is encountered in the design table when updating the design table, false to not

## VBA Syntax

See [DesignTable::Warn](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~Warn.html).

## Remarks

If information is entered to the left of the parameters row or below the configuration name column, then the SOLIDWORKS Design software warns of an invalid value and stops processing the design table without completing the remaining rows and columns. If this happens, some configurations do not update properly.

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html) after setting this property.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::UpdateTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
