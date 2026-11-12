---
title: "GetNameForSelection Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetNameForSelection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetNameForSelection.html"
---

# GetNameForSelection Method (IDimension)

Gets the name of the selected dimension needed by [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNameForSelection() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.String

value = instance.GetNameForSelection()
```

### C#

```csharp
System.string GetNameForSelection()
```

### C++/CLI

```cpp
System.String^ GetNameForSelection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of selected dimension

## VBA Syntax

See [Dimension::GetNameForSelection](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetNameForSelection.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDisplayDimension::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetNameForSelection.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
