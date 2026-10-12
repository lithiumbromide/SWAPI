---
title: "Attach3 Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "Attach3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.html"
---

# Attach3 Method (IBomTable)

Activates the BOM.

## Syntax

### Visual Basic (Declaration)

```vb
Function Attach3() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim value As System.Boolean

value = instance.Attach3()
```

### C#

```csharp
System.bool Attach3()
```

### C++/CLI

```cpp
System.bool Attach3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successfully attached, false if not

## VBA Syntax

See [BomTable::Attach3](ms-its:sldworksapivb6.chm::/sldworks~BomTable~Attach3.html).

## Remarks

If you want SOLIDWORKS to run in the background, then do not use this method. Using this method will cause SOLIDWORKS to become visible.

You must call this method before using any of the [IBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable.html) methods.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
