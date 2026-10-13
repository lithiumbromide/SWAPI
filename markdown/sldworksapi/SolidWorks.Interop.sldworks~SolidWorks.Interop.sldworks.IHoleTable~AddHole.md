---
title: "AddHole Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "AddHole"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~AddHole.html"
---

# AddHole Method (IHoleTable)

Adds holes to this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddHole() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Integer

value = instance.AddHole()
```

### C#

```csharp
System.int AddHole()
```

### C++/CLI

```cpp
System.int AddHole();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of holes added to this hole table

## VBA Syntax

See [HoleTable::AddHole](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~AddHole.html).

## Remarks

You must either interactively or programmatically select the holes to add to the hole table before running this method.

| To add holes... | Then... |
| --- | --- |
| Interactively | Select an edge that defines a hole to add that hole to this hole table. Select a face that contains the holes that you want to add to this hole table. |
| Programatically | Call IModelDocExtension::SelectByID2 . |

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
