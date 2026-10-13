---
title: "HasDesignTable Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HasDesignTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasDesignTable.html"
---

# HasDesignTable Method (IModelDocExtension)

Gets whether a document has a design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasDesignTable() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.HasDesignTable()
```

### C#

```csharp
System.bool HasDesignTable()
```

### C++/CLI

```cpp
System.bool HasDesignTable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if document has a design table, false if not (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::HasDesignTable](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~HasDesignTable.html).

## Examples

[Delete Design Table (VBA)](Delete_Design_Table_Example_VB.htm)

## Remarks

This method always returns false for drawing documents because in drawing documents the design table is attached to the drawing view and not the document. Use [IView::HasDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~HasDesignTable.html) to determine if a drawing view in a drawing document has a design table.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
