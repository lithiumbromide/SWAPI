---
title: "Select Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~Select.html"
---

# Select Method (IAdvancedSelectionCriteria)

Selects the assembly components that satisfy the current advanced selection criteria.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim value As System.Boolean

value = instance.Select()
```

### C#

```csharp
System.bool Select()
```

### C++/CLI

```cpp
System.bool Select();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the components are selected, false if not

## VBA Syntax

See [AdvancedSelectionCriteria::Select](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~Select.html).

## Examples

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html) examples.

## Remarks

Call this method after either:

- [Loading](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~LoadCriteria.html) the criteria from a ***.xml** file or a ***.sqy** legacy file.

- or -

- [Adding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.html) items to the advanced component selection criteria list.

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
