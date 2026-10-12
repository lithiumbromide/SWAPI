---
title: "GetSelectionFocus Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "GetSelectionFocus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectionFocus.html"
---

# GetSelectionFocus Method (IPropertyManagerPageSelectionbox)

Gets whether this is the active selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionFocus() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean

value = instance.GetSelectionFocus()
```

### C#

```csharp
System.bool GetSelectionFocus()
```

### C++/CLI

```cpp
System.bool GetSelectionFocus();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selection box is active, false if not

## VBA Syntax

See [PropertyManagerPageSelectionbox::GetSelectionFocus](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~GetSelectionFocus.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
