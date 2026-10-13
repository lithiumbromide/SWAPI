---
title: "IsDesignTableDimension Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IsDesignTableDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsDesignTableDimension.html"
---

# IsDesignTableDimension Method (IDimension)

Gets whether this dimension is driven by a design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDesignTableDimension() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Boolean

value = instance.IsDesignTableDimension()
```

### C#

```csharp
System.bool IsDesignTableDimension()
```

### C++/CLI

```cpp
System.bool IsDesignTableDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the dimension is driven by a design table, false if not

## VBA Syntax

See [Dimension::IsDesignTableDimension](ms-its:sldworksapivb6.chm::/sldworks~Dimension~IsDesignTableDimension.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::DrivenState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DrivenState.html)
[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
