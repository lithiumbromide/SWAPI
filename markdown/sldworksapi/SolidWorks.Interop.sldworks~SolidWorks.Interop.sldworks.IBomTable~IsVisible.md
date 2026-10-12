---
title: "IsVisible Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "IsVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~IsVisible.html"
---

# IsVisible Method (IBomTable)

Gets whether this BOM is visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsVisible() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim value As System.Boolean

value = instance.IsVisible()
```

### C#

```csharp
System.bool IsVisible()
```

### C++/CLI

```cpp
System.bool IsVisible();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the BOM is visible, false if not

## VBA Syntax

See [BomTable::IsVisible](ms-its:sldworksapivb6.chm::/sldworks~BomTable~IsVisible.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
