---
title: "CustomPropertyManager Property (ICutListItem)"
project: "SOLIDWORKS API Help"
interface: "ICutListItem"
member: "CustomPropertyManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem~CustomPropertyManager.html"
---

# CustomPropertyManager Property (ICutListItem)

Gets the custom property manager for this configuration-specific cut list.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CustomPropertyManager As CustomPropertyManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICutListItem
Dim value As CustomPropertyManager

value = instance.CustomPropertyManager
```

### C#

```csharp
CustomPropertyManager CustomPropertyManager {get;}
```

### C++/CLI

```cpp
property CustomPropertyManager^ CustomPropertyManager {
   CustomPropertyManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)

## VBA Syntax

See [CutListItem::CustomPropertyManager](ms-its:sldworksapivb6.chm::/sldworks~CutListItem~CustomPropertyManager.html).

## See Also

[ICutListItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem.html)
[ICutListItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem_members.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
