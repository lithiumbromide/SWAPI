---
title: "GetCutListItems Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetCutListItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCutListItems.html"
---

# GetCutListItems Method (IConfiguration)

Gets the cut list folders in this active or non-active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCutListItems() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Object

value = instance.GetCutListItems()
```

### C#

```csharp
System.object GetCutListItems()
```

### C++/CLI

```cpp
System.Object^ GetCutListItems();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [ICutListItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem.html)s

## VBA Syntax

See [Configuration::GetCutListItems](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetCutListItems.html).

## Examples

See the [ICutListItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem.html) examples.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
