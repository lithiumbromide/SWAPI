---
title: "GetTitle Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetTitle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTitle.html"
---

# GetTitle Method (IDesignTable)

Gets the design table title.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTitle() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.String

value = instance.GetTitle()
```

### C#

```csharp
System.string GetTitle()
```

### C++/CLI

```cpp
System.String^ GetTitle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Design table title

## VBA Syntax

See [DesignTable::GetTitle](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetTitle.html).

## Examples

[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

## Remarks

This method returns the title of the design table. If the title row is absent, then this method returns an empty string. If the title row exists but there is no title, then this method returns a single space.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
