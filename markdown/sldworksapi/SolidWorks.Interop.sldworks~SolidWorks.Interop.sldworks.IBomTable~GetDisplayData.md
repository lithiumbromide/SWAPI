---
title: "GetDisplayData Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetDisplayData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetDisplayData.html"
---

# GetDisplayData Method (IBomTable)

Returns the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object for this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim value As System.Object

value = instance.GetDisplayData()
```

### C#

```csharp
System.object GetDisplayData()
```

### C++/CLI

```cpp
System.Object^ GetDisplayData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Display data for this BOM table

## VBA Syntax

See [BomTable::GetDisplayData](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetDisplayData.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::IGetDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~IGetDisplayData.html)
