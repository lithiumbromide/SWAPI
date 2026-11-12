---
title: "UpdateModel Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "UpdateModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.html"
---

# UpdateModel Method (IDesignTable)

Applies the edits to the design table to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateModel() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

value = instance.UpdateModel()
```

### C#

```csharp
System.bool UpdateModel()
```

### C++/CLI

```cpp
System.bool UpdateModel();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the model is updated successfully, false if it was not

## VBA Syntax

See [DesignTable::UpdateModel](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~UpdateModel.html).

## Remarks

This method is a simplified version of [IDesignTable::UpdateTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~UpdateTable.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::EditFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html)
[IDesignTable::EditTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.html)
[IDesignTable::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.html)
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html)
[IDesignTable::Updatable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Updatable.html)
[IDesignTable::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.html)

## Availability

SOLIDWORKS 2000 SP01, Revision Number 8.1
