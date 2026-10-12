---
title: "IGetDisplayData Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "IGetDisplayData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~IGetDisplayData.html"
---

# IGetDisplayData Method (IBomTable)

Returns the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object for this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDisplayData() As DisplayData
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim value As DisplayData

value = instance.IGetDisplayData()
```

### C#

```csharp
DisplayData IGetDisplayData()
```

### C++/CLI

```cpp
DisplayData^ IGetDisplayData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer for the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) for this BOM table

## VBA Syntax

See [BomTable::IGetDisplayData](ms-its:sldworksapivb6.chm::/sldworks~BomTable~IGetDisplayData.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::GetDisplayData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetDisplayData.html)
